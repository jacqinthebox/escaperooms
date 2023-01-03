<script>
    import {Router, Route, Link} from 'svelte-routing'
    import Home from './Home.svelte'
    import About from './About.svelte'
    import Register from './Register.svelte'
    import Login from './Login.svelte'
    import Logout from './Logout.svelte'

    function getCookie(name) {
        let value = "; " + document.cookie;
        let parts = value.split("; " + name + "=");
        if (parts.length === 2) return parts.pop().split(";").shift();
    }

    let url = "";
    let emailPresent = getCookie('email');
    let teamName = getCookie('teamName');
</script>

<Router url="{url}">
    <!-- svelte-ignore a11y-no-redundant-roles -->
    <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
            <a class="navbar-item" href="/">
                <h1 class="title is-5">The Escape Room Tracer</h1>
            </a>

            <!-- svelte-ignore a11y-missing-attribute -->
            <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
                <a class="navbar-item" href="/about">
                    About </a>
            </div>

            <div class="navbar-end">
                <div class="navbar-item has-dropdown is-hoverable">
                    <!-- svelte-ignore a11y-missing-attribute -->
                    {#if emailPresent}
                        <a class="navbar-link">{emailPresent}</a>
                    {:else }
                        <a class="navbar-link">Menu</a>
                    {/if}
                    <div class="navbar-dropdown">
                        {#if emailPresent}
                            <a class="navbar-item" href="/logout">Logout</a>
                        {:else}
                            <a class="navbar-item" href="/login">Login</a>
                        {/if}
                        <a class="navbar-item" href="/register">Register</a>
                        <a class="navbar-item" href="/about">About</a>
                    </div>

                </div>
                <div class="navbar-item">
                    <!-- svelte-ignore a11y-invalid-attribute -->
                    {#if !emailPresent}
                        <a class="button is-primary" href="/register">
                            <strong>Register</strong>
                        </a>
                    {:else}
                        <a class="button is-primary" href="/logout">
                            <strong>Logout</strong>
                        </a>
                    {/if}
                </div>
            </div>
        </div>
    </nav>
    <div>
        <Route path="/">
            <Home/>
        </Route>
        <Route path="about">
            <About/>
        </Route>
        <Route path="register">
            <Register/>
        </Route>
        <Route path="login">
            <Login/>
        </Route>
        <Route path="logout">
            <Logout/>
        </Route>
    </div>
</Router>
