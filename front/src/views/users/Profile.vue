<template>
  <div class="row justify-center no-wrap" style="width: 100%">
    <Menu
      id="profile-menu"
      :active-section="activeSection"
      @setActiveSection="setSection($event)"
    />
    <router-view class="col-8" :section="activeSection" />
  </div>

  <br />
</template>

<script setup lang="ts">
import { ref } from "vue";
import Menu from "@/components/profile/Menu.vue";

const activeSection = ref("general");

function setSection(section) {
  activeSection.value = section;
}
</script>

<style>
#profile-menu {
  align-self: baseline;
}
</style>
