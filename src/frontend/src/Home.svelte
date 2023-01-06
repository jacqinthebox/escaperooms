<script>
    import {onMount} from 'svelte';
    import {redirect} from './store.js';
    import Login from './Login.svelte'
    //import Cookies from 'js-cookie';
    let email = ''
    let teamName = ''
    let encodedTeamName = ''
    let spacelessTeamName = ''
    let elapsedTime = ''
    window.elapsedTime = elapsedTime;
    let inRoom = false;
    let displayText = "";
    let sentences = ["Solving a nice puzzle..", "Solving puzzle..", "Solving another puzzle...", "Fighting this riddle...", "Freaking out over a puzzle...", "Want to get out but I'm not finished..."];
    let intervalId;
    let startTime;
    let showLink = false;

    console.log(process.env.API_URL);

    let apiUrl = '';
    let roomApiUrl = '';

    onMount(() => {
        apiUrl = `${window.location.protocol}//${window.location.host}`;
        const hostParts = window.location.host.split(':');
        const host = hostParts[0];

        if (host === '127.0.0.1' || host === '0.0.0.0' || host === 'localhost') {
            apiUrl = `${window.location.protocol}//${host}:5000`;
            roomApiUrl = `${window.location.protocol}//${host}:5005`;
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
            email = getCookie('email')
            encodedTeamName = getCookie('teamName')
            teamName = decodeURIComponent(encodedTeamName)
            spacelessTeamName = teamName.replace(/\s/g, '')
        }
    });

    console.log("inRoom is now " + inRoom)

    function enterRoom() {
        inRoom = true;
        startTime = new Date();
        intervalId = setInterval(() => {
            displayText = sentences[Math.floor(Math.random() * sentences.length)];
        }, 1000);
        console.log("inRoom is now " + inRoom)
    }

    function leaveRoom() {
        inRoom = false;
        showLink = true;
        clearInterval(intervalId)
        const endTime = new Date();
        const elapsedTime = (endTime - startTime) / 1000; // elapsed time in seconds
        const minutes = Math.floor(elapsedTime / 60);
        const seconds = Math.floor(elapsedTime % 60);
        displayText = teamName + " has left the escape room after " + minutes + " minutes and " + seconds + "  seconds. Well done!";
        window.elapsedTime = elapsedTime

    }

    async function checkAPI() {
        try {
            const response = await fetch(roomApiUrl + '/room/ping');
            if (response.ok) {
                console.log('API is active');
            } else {
                console.log('API is not active');
            }
        } catch (error) {
            console.log('API is not active');
        }
    }

    async function postResult() {
        await checkAPI();
        const response = fetch(roomApiUrl + '/room/leave', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                team: spacelessTeamName,
                email: email,
                elapsedSeconds: window.elapsedTime
            })
        });
        showLink = false
    }


</script>

<main>
    <section class="section">

        {#if $redirect !== null}
            <div class="container">
                <Login/>
            </div>
        {:else}
            <div class="container">
                <h1 class="title">Hi team {teamName}! </h1>
                <h2 class="subtitle">You can now enter the escape room.</h2>
                <p>Good luck!</p>

                <div class="section">
                    <button class="button is-primary" disabled={inRoom} on:click={enterRoom}>Enter escape room</button>
                    <button class="button is-danger" disabled={!inRoom} on:click={leaveRoom}>Leave escape room</button>
                    <p>{displayText}</p>
                </div>
                <div class="section">
                    <button class="button is-info" disabled={!showLink} on:click={postResult}>Post escape result</button>
                </div>

            </div>
        {/if}
    </section>

</main>
