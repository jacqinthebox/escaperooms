<script>
    import {onMount} from 'svelte';
    import {redirect} from './store.js';
    import Login from './Login.svelte'
    //import Cookies from 'js-cookie';
    let email = ''
    let teamName = ''
    console.log(process.env.API_URL);

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
