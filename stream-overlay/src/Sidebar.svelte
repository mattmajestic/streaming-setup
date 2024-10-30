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
    font-size: 2.2rem;
    border-radius: 8px;
    background-color: var(--social-color, #333);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
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
    background: #000000; /* Black background */
    border-radius: 8px;
    height: 30vh;
    overflow: hidden;
    font-size: 2.0rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    padding: 10px;
    display: flex;
    color: white;
    flex: 1;
  }

  /* Chat section */
  #chat {
    background: #000000; /* Black background */
    border-radius: 8px;
    padding: 10px;
    font-size: 2.0rem;
    overflow-y: auto;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    flex: 1;
  }

  /* Logo styling - smaller size */
  .social-logo {
    width: 12%; /* Reduced logo size */
    height: auto;
    margin-right: 8px;
  }

  /* Style for icon text alignment */
  .icon-text {
    display: flex;
    flex-direction: column;
    align-items: center;
    font-size: 2rem;
  }

  /* Keyframes for bouncing animation */
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
      transform: translateY(0);
    }
    40% {
      transform: translateY(-10px);
    }
    60% {
      transform: translateY(-5px);
    }
  }

  /* Apply bounce animation to icons */
  .icon {
    font-size: 2.5rem;
    margin-bottom: 5px;
    animation: bounce 5s infinite;
  }
</style>

<div id="sidebar">
  <!-- Dynamic socials box in the bottom left corner -->
  <div id="socials" data-platform={socialPlatform.name}>
    <img src={socialPlatform.logoSrc} alt="{socialPlatform.name} Logo" class="social-logo" />
    @{socialPlatform.username}
  </div>

  <!-- Chat section with icon and text on separate lines -->
  <div id="chat" class="icon-text">
    <span class="icon">💬</span>
    <span>Chat</span>
  </div>

  <!-- Camera section with icon and text on separate lines -->
  <div id="camera" class="icon-text">
    <span class="icon">📷</span>
    <span>Code</span>
    <span>Cam</span>
  </div>
</div>
