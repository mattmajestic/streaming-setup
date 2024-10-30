<script lang="ts">
  import { onMount } from 'svelte';
  import { fade } from 'svelte/transition';

  const socialPlatforms = [
    {
      name: 'YouTube',
      username: 'MajesticCoding',
      color: '#FF0000',
      logoSrc: '/youtube-color.svg'
    },
    {
      name: 'GitHub',
      username: 'mattmajestic',
      color: '#4A4A4A',
      logoSrc: '/github-color.svg'
    },
    {
      name: 'Twitch',
      username: 'MajesticCodingTwitch',
      color: '#6441a4',
      logoSrc: '/twitch-color.svg'
    }
  ];

  let currentPlatformIndex = 0;
  let socialPlatform = socialPlatforms[currentPlatformIndex];

  onMount(() => {
    const interval = setInterval(() => {
      currentPlatformIndex = (currentPlatformIndex + 1) % socialPlatforms.length;
      socialPlatform = socialPlatforms[currentPlatformIndex];
    }, 15000);

    return () => clearInterval(interval);
  });
</script>

<style>
  /* Socials styling */
  #socials {
    position: absolute;
    bottom: 20px;
    left: 20px;
    display: flex;
    align-items: center;
    padding: 8px 16px;
    color: white;
    font-size: 1.5rem;
    border-radius: 8px;
    background-color: var(--social-color, #333);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    transition: background-color 0.5s ease;
    /* Remove any unnecessary container background */
    overflow: hidden;
  }

  #socials[data-platform="YouTube"] {
    --social-color: #FF0000;
  }
  #socials[data-platform="GitHub"] {
    --social-color: #4A4A4A;
  }
  #socials[data-platform="Twitch"] {
    --social-color: #6441a4;
  }

  /* Logo styling */
  .social-logo {
    width: 24px;
    height: auto;
    margin-right: 10px;
  }
</style>

<!-- Apply the fade transition to the whole component -->
{#if socialPlatform}
  <div id="socials" data-platform={socialPlatform.name} in:fade={{ duration: 500 }}>
    <img src={socialPlatform.logoSrc} alt="{socialPlatform.name} Logo" class="social-logo" />
    @{socialPlatform.username}
  </div>
{/if}
