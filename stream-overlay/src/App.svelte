<script lang="ts">
  import MainScreen from './MainScreen.svelte';
  import Sidebar from './Sidebar.svelte';
  import Promotions from './Promotions.svelte';
</script>

<style>
  /* Reset margins and set box-sizing for consistent sizing */
  html, body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    overflow: hidden;
    width: 100vw;
    height: 100vh;
  }

  *, *::before, *::after {
    box-sizing: inherit;
  }

  /* Outer wrapper for the glowing border */
  #outer-wrapper {
    width: 100vw;
    height: 100vh;
    padding: 10px; /* Space around to show glow */
    background-color: #000; /* Dark background */
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    border-radius: 10px;

    /* Glowing border with animated gradient */
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.3), 0 0 40px rgba(0, 255, 255, 0.5), 0 0 60px rgba(0, 255, 255, 0.7);
    animation: gradientGlow 6s linear infinite;
  }

  /* Full-screen overlay with reduced width/height for border visibility */
  #overlay {
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 10fr 1fr; /* Sidebar size adjustment */
    gap: 10px;
    background-color: #000;
    color: #fff;
    position: relative;
    border-radius: 10px;
  }

  /* Bottom-center position for Promotions */
  #promotions {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1; /* Make sure it’s on top of the overlay */
  }

  /* Keyframes for animated gradient glow */
  @keyframes gradientGlow {
    0% {
      box-shadow: 0 0 10px rgba(0, 150, 150, 0.3), 0 0 20px rgba(0, 200, 200, 0.5), 0 0 30px rgba(0, 255, 255, 0.7);
    }
    50% {
      box-shadow: 0 0 30px rgba(0, 200, 200, 0.4), 0 0 40px rgba(0, 255, 255, 0.6), 0 0 50px rgba(0, 255, 255, 0.8);
    }
    100% {
      box-shadow: 0 0 10px rgba(0, 150, 150, 0.3), 0 0 20px rgba(0, 200, 200, 0.5), 0 0 30px rgba(0, 255, 255, 0.7);
    }
  }
</style>

<div id="outer-wrapper">
  <div id="overlay">
    <MainScreen />
    <Sidebar />
  </div>
  <div id="promotions">
    <Promotions />
  </div>
</div>
