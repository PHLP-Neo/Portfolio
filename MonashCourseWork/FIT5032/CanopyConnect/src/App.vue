<script setup>
  import BHeader from './components/BHeader.vue'
</script>

<template>
  <a href="#main-content" class="skip-link">
    Skip to main content
  </a>
  <header class="site-header">
    <BHeader />
  </header>

  <main id="main-content" tabindex="-1">
    <router-view></router-view>
  </main>
</template>