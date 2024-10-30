<script lang="ts">
  import MainScreen from './MainScreen.svelte';
  import Sidebar from './Sidebar.svelte';
  import Socials from './Socials.svelte';
  import Promotions from './Promotions.svelte';
</script>

<style>
  /* Reset margins and set box-sizing for consistent sizing */
  html, body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    overflow: hidden; /* Prevent any scrollbars */
  }

  *, *::before, *::after {
    box-sizing: inherit;
  }

  /* Full-screen overlay using viewport width and height */
  #overlay {
    width: 100vw;
    height: 100vh;
    display: grid;
    grid-template-columns: 10fr 1fr; /* Makes the sidebar smaller */
    gap: 10px;
    background-color: #121212; /* Dark theme background */
    color: #fff;
    overflow: hidden; /* Ensures no overflow */
    position: relative; /* Allows absolute positioning for Socials and Promotions */
  }

  /* Bottom-left position for Socials */
  #socials {
    position: absolute;
    left: 20px;
    bottom: 20px;
  }

  /* Bottom-center position for Promotions */
  #promotions {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
  }
</style>

<div id="overlay">
  <MainScreen />
  <Sidebar />

  <div id="promotions">
    <Promotions />
  </div>
</div>
