<script>

  import { Link, Router, Route } from "svelte-routing";
  import About from './About.svelte'
  export let toggleRegisterForm;
  export let url = "";
</script>




<Router url="{url}">
<!-- svelte-ignore a11y-no-redundant-roles -->
<nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/public">
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
        <a class="navbar-item" href="/public">
          Home
        </a>
      </div>

      <div class="navbar-end">
            <div class="navbar-item has-dropdown is-hoverable">
            <!-- svelte-ignore a11y-missing-attribute -->
            <a class="navbar-link">email</a>
            <div class="navbar-dropdown">
                    <Link to="about" class="navbar-item">About</Link>
                    <Link to="logout" class="navbar-item">Logout</Link>
            </div>

          </div>
          <div class="navbar-item">
            <!-- svelte-ignore a11y-invalid-attribute -->
            <a class="button is-primary" href="#" on:click={toggleRegisterForm}>
              <strong>Sign up</strong>
            </a>
          </div>
      </div>
    </div>
  </nav>
    <Route path="about" component="{About}" />
</Router>


