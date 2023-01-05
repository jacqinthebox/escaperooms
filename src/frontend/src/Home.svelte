<script>
    import {onMount} from 'svelte';
    import {redirect} from './store.js';
    import Login from './Login.svelte'
    //import Cookies from 'js-cookie';
    let email = ''
    let teamName = ''
    console.log(process.env.API_URL);

    let apiUrl = '';

    onMount(() => {
        apiUrl = `${window.location.protocol}//${window.location.host}`;
        const hostParts = window.location.host.split(':');
        const host = hostParts[0];

        if (host === '127.0.0.1' || host === '0.0.0.0' || host === 'localhost') {
            apiUrl = `${window.location.protocol}//${host}:5000`;
        }
    });



    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) {
            return parts.pop().split(';').shift();
        }
    }

    onMount(() => {
        if (!getCookie('email')) {
            console.log("No email cookie")
            redirect.set('/login');
            console.log("Generated api url: " + apiUrl + "/api")
            console.log($redirect)
        } else {
            //there is a cookie and we can use its value
            //email = Cookies.get('email')
            console.log("Yippie")
            teamName = getCookie('teamName')
        }
    });
</script>

<main>
    <section class="section">

        {#if $redirect !== null}
            <Login/>
        {:else}
            <h1>Hi {teamName}! </h1>
            <p>Are you ready for an amazing Escaperoom adventure?</p>
        {/if}

    </section>
</main>
