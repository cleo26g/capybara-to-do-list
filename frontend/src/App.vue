<template>
  <div>
    <div class=".container-fluid">
      <SignedOutNavBar v-if="!isSignedIn"/>
      <div v-if="error" id="errorMessage" class="alert alert-warning position-fixed" role="alert">
        <button type="button" class="btn-close" aria-label="Close" @click="closeError()"></button>
        {{error}}
      </div>
      <authenticator
        :login-mechanisms="['email']"
      >
        <template v-slot="{ user, signOut }">
          <MainNavBar :user=user :signOut=signOut :isAuthenticated="isSignedIn"/>
          <MainAppHero />
          <div class="btn-group mainButtonGroup" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-primary" @click="getAllPosts">Get All Posts</button>
            <button type="button" class="btn btn-success" @click="createPost">Create Post</button>
          </div>
          <ViewAuthTokenModalAndButton :authToken="authToken" />
        </template>
      </authenticator>
      <form v-if="isSignedIn">
        <div class="px-4 my-5 text-center">
          <label for="postText" class="form-label">Write your post:</label>
          <input
            v-model="newPostSubmission"
            type="email"
            class="form-control mx-auto p-2"
            style="width: 60%;"
            id="postText"
            aria-describedby="emailHelp"
            placeholder="Your feedback here..."
          >
        </div>
      </form>
      <div v-if="isSignedIn">
        <div
            v-for="post in allPosts"
            :key="post.postId"
        >
          <UserPost :post="post" :deletePost="this.deletePost" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Authenticator, useAuthenticator } from '@aws-amplify/ui-vue';
import { Amplify } from 'aws-amplify';
import '@aws-amplify/ui-vue/styles.css';
import MainAppHero from './components/MainAppHero.vue';
import MainNavBar from './components/MainNavBar.vue';
import SignedOutNavBar from './components/SignedOutNavBar.vue';
import UserPost from './components/UserPost.vue';
import ViewAuthTokenModalAndButton from './components/ViewAuthTokenModalAndButton.vue';

const auth = useAuthenticator();

const API_ENDPOINT = 'REPLACE_ME'

export default {
  components: {
    MainAppHero,
    MainNavBar,
    SignedOutNavBar,
    UserPost,
    ViewAuthTokenModalAndButton,
    Authenticator,
  },
  computed: {
    isSignedIn() {
      return auth.authStatus === 'authenticated'
    },
  },
  data () {
    return {
      newPostSubmission: '',
      allPosts: [],
      authToken: 'The auth token has not been generated yet.',
      error: '',
    };
  },
  methods: {
    closeError() {
      this.error = '';
    },
    async getAuthToken() {
      const session = await Amplify.Auth.currentSession();
      const token = session.getIdToken().getJwtToken();
      this.authToken = token;
      return 'Bearer ' + token;
    },
    async deletePost(userId, postId) {
      const response = await fetch(API_ENDPOINT + '/user/' + userId + '/post/' + postId, {
        method: 'DELETE',
        headers: {
          Authorization: await this.getAuthToken(),
        },
      });
      // If successfully deleted, update the page
      if (response.status === 200) {
        this.getAllPosts();
      }
      if (response.status !== 200) {
        this.error = "You do not have permission to delete this post."
      }
    },
    async createPost() {
      const response = await fetch(API_ENDPOINT + '/user/post', {
        method: 'POST',
        headers: {
          Authorization: await this.getAuthToken(),
        },
        body: JSON.stringify({
          post: this.newPostSubmission,
        }),
      });
      // If successfully posted, update the page
      if (response.status === 200) {
        this.getAllPosts();
      }
    },
    async getAllPosts() {
      const response = await fetch(API_ENDPOINT + '/user/posts', {
        headers: {
          Authorization: await this.getAuthToken(),
        },
      });
      const data = await response.json();
      this.allPosts = data;
    },
  },
};
</script>

<style scoped>
body {
  background-color: #f5f5f5;
}

#app {
  width: 100%;
}

.mainButtonGroup {
  margin: 10px;
  display: table;
  margin-left: auto;
  margin-right: auto;
}

.form-label {
  font-size: 28px;
}

#errorMessage {
  width: 100%;
  z-index: 1000;
}
</style>