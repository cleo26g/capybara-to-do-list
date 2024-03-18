<template>
    <nav id="mainNavbar" class="navbar bg-secondary" data-bs-theme="dark">
        <div class="container-fluid">
            <a class="navbar-brand">Cognito Group Auth Demo</a>
            <span class="navbar-text ms-auto me-2">
                Welcome {{ user.attributes.email }}!
            </span>
            <button
                v-if="isAuthenticated"
                type="button"
                class="btn btn-info"
                @click="signOut">
                Sign Out
            </button>
        </div>
    </nav>    
</template>

<script>
export default {
    name: 'MainNavBar',
    props: {
        user: {
            type: Object,
            required: true
        },
        signOut: {
            type: Function,
            required: true
        },
        isAuthenticated: {
            type: Boolean,
            required: true
        }
    }
}
</script>

<style scoped>
#mainNavbar {
  background-color: #0D37A0 !important;
}
</style>