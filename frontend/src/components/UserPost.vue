<template>
<div>
    <div class="card px-4 my-5 mx-auto p-2" style="width: 60%;">
    <div class="card-body">
        <h5 class="card-title">User {{post.userId.split("-")[0]}} says:</h5>
        <p class="card-text">{{post.postData.post}}</p>
        <button type="button" class="btn btn-warning" @click="deletePost(post.userId, post.postId)">Delete Post (Admin Only)</button>
    </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'UserPost',
    props: {
        post: {
            type: Object,
            required: true
        },
        deletePost: {
            type: Function,
            required: true
        }
    }
}
</script>