<template>
    <div>
      <img src="architecture.png" width="1000px">
      <span />
      <v-btn x-large block @click="login">
        Go to dashboard
      </v-btn>
    </div>
</template>

<script>
   import axios from 'axios'
   export default {
       name: 'Home',
       data () {
         return {
           isLoggedIn: false,
           baseUrl: 'http://soa.servehttp.com'
         }
       },
       created () {
         this.updateIsLoggedIn()
       },
       methods: {
         login () {
           window.location = this.baseUrl + '/auth/google'
         },
         updateIsLoggedIn () {
           this.$router.push('dashboard');
           const uri = this.baseUrl + '/novatrends/auth/check'
           axios.post(uri, {}).then(response => {
             this.isLoggedIn = response.data.auth;
             if(this.isLoggedIn){
                this.$router.push('dashboard');
             }
           }).catch( (e) => {
              console.log(e)
              this.isLoggedIn = false;
           });
         },
       },
     }
</script>