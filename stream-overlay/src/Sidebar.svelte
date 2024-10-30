<script lang="ts">
  import { onMount } from 'svelte';

  // Define the social media data with SVG paths, usernames, and colors
  const socialPlatforms = [
    {
      name: 'YouTube',
      username: 'MajesticCoding',
      color: '#FF0000', // YouTube red
      logoSrc: '/youtube-color.svg'
    },
    {
      name: 'GitHub',
      username: 'mattmajestic',
      color: '#4A4A4A', // Light grey for GitHub
      logoSrc: '/github-color.svg'
    },
    {
      name: 'Twitch',
      username: 'MajesticCodingTwitch',
      color: '#6441a4', // Twitch purple
      logoSrc: '/twitch-color.svg'
    }
  ];

  // Reactive variables for the current social platform
  let currentPlatformIndex = 0;
  let socialPlatform = socialPlatforms[currentPlatformIndex];

  // Function to rotate social platforms every 30 seconds
  onMount(() => {
    const interval = setInterval(() => {
      currentPlatformIndex = (currentPlatformIndex + 1) % socialPlatforms.length;
      socialPlatform = socialPlatforms[currentPlatformIndex];
    }, 30000); // 30-second interval

    return () => clearInterval(interval); // Cleanup on unmount
  });
</script>

<style>
  /* Overall Sidebar layout */
  #sidebar {
    display: flex;
    flex-direction: column;
    height: 100%;
    gap: 10px;
  }

  /* Socials section positioned at the bottom left corner */
  #socials {
    position: absolute;
    bottom: 20px;
    left: 20px;
    display: flex;
    align-items: center;
    padding: 8px 12px;
    color: white;
    font-size: 1.5rem;
    border-radius: 8px;
    background-color: var(--social-color, #333);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    border: 2px solid rgba(255, 255, 255, 0.1); /* Subtle border */
    transition: background-color 0.5s ease;
  }

  /* Dynamic background color for socials */
  #socials[data-platform="YouTube"] {
    --social-color: #FF0000;
  }
  #socials[data-platform="GitHub"] {
    --social-color: #4A4A4A;
  }
  #socials[data-platform="Twitch"] {
    --social-color: #6441a4;
  }

  /* Camera section styling */
  #camera {
    background: #2e2e2e; /* Dark grey background */
    border: 2px solid rgba(0, 255, 255, 0.3); /* Aqua hint border */
    border-radius: 8px;
    height: 30vh;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
  }

  /* Chat section */
  #chat {
    background: #333;
    border-radius: 8px;
    padding: 10px;
    overflow-y: auto;
    flex: 1;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  }

  /* Logo styling - smaller size */
  .social-logo {
    width: 12%; /* Reduced logo size */
    height: auto;
    margin-right: 8px;
  }
</style>

<div id="sidebar">
  <!-- Dynamic socials box in the bottom left corner -->
  <div id="socials" data-platform={socialPlatform.name}>
    <img src={socialPlatform.logoSrc} alt="{socialPlatform.name} Logo" class="social-logo" />
    @{socialPlatform.username}
  </div>
  
  

  <!-- Chat section above camera -->
  <div id="chat">
    Chat
  </div>

  <!-- Camera section with colored border -->
  <div id="camera">
    Camera
  </div>
</div>
