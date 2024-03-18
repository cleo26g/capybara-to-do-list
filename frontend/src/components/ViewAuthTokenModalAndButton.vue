<template>
    <div>
        <div id="authTokenButton" class="btn-group" role="group" aria-label="Basic example">
            <button type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#exampleModal">View Auth Token</button>
        </div>
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">
                <div v-if="authTokenCopied" class="alert alert-info" role="alert">
                    Auth Token Copied
                </div>
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Auth Token</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="this.authTokenCopied=false"></button>
                </div>
                <div class="modal-body">
                    {{authToken}}
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="this.authTokenCopied=false">Close</button>
                    <button type="button" class="btn btn-primary" @click="copyText">Copy Token</button>
                </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
export default {
    name: 'MainNavBar',
    props: {
        authToken: {
            type: String,
            required: true,
        }
    },
    data () {
        return {
            authTokenCopied: false,
        };
    },
    methods: {
        copyText() {
            navigator.clipboard.writeText(this.authToken);
            this.authTokenCopied = true;
        },
    }
}
</script>

<style scoped>
#authTokenButton {
  margin: 10px;
  display: table;
  margin-left: auto;
  margin-right: auto;
}
</style>