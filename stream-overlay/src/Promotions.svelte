<script lang="ts">
  import { onMount } from 'svelte';
  import messages from './messages.json'; // Import JSON file directly

  // State to track the current message
  let currentMessageIndex = 0;
  let currentMessage = messages[currentMessageIndex];

  // Rotate messages every 15 seconds
  onMount(() => {
    const interval = setInterval(() => {
      currentMessageIndex = (currentMessageIndex + 1) % messages.length;
      currentMessage = messages[currentMessageIndex];
    }, 15000); // Set the interval to 15 seconds

    return () => clearInterval(interval); // Cleanup on unmount
  });
</script>

<style>
  /* Styling for the Promotions component */
  #promotions {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px 12px;
    color: white;
    font-size: 1.2rem;
    border-radius: 8px;
    background: linear-gradient(135deg, #333, #555); /* Dark gradient background */
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
    border: 2px solid rgba(255, 255, 255, 0.15); /* Subtle border */
    transition: opacity 0.5s ease; /* Smooth fade effect */
    height: 4vh; /* Set to half height as per request */
    width: fit-content;
    text-align: center;
  }

  /* Refined Fade Animation */
  @keyframes fade {
    0% { opacity: 0; }
    15% { opacity: 1; }
    85% { opacity: 1; }
    100% { opacity: 0; }
  }

  /* Apply fade animation with correct duration */
  #promotions {
    animation: fade 15s infinite; /* Sync with message rotation */
  }
</style>

<div id="promotions">
  {currentMessage}
</div>
