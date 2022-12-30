<script>
	import { Router, Route, Link } from "svelte-routing";
	import Navbar from './components/Navbar.svelte'
	import Register from './components/Register.svelte';
	import LoginForm from './components/LoginForm.svelte';
	import Success from './components/Success.svelte';

	import About from './components/About.svelte';
	import { onMount } from 'svelte';
	export let url = "";
    // https://dev.to/lukocastillo/svelte-3-how-to-connect-your-app-with-a-rest-api-axios-2h4e
	// https://linguinecode.com/post/how-to-add-routes-to-svelte-spa-with-routify

	let showLoginForm = false;
	let showRegisterForm =  false;

	onMount(() => {
		const emailCookie = getCookie('email');
		if (!emailCookie) {
		showLoginForm = true;
		}
		document.cookie = "username=John Doe";
	});

	function getCookie(name) {
		const value = `; ${document.cookie}`;
		const parts = value.split(`; ${name}=`);
			if (parts.length === 2) {
			return parts.pop().split(';').shift();
		}
	}

	function toggleRegisterForm() {
    	showRegisterForm = !showRegisterForm;
		showLoginForm = !showLoginForm;
  	}
</script>

<Router>
  <Route path="/login" component={LoginForm} />
  <Route path="/success" component={Success} />
</Router>



<!-- Your app or component template goes here -->
<main>
	<Navbar toggleRegisterForm={toggleRegisterForm} />
	{#if showLoginForm}
		<LoginForm />
	{/if}

	{#if showRegisterForm}
  		<Register />
	{/if}
  	<!-- <Register /> -->

</main>
