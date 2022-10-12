<script setup lang="ts">
import Menu from "../../components/profile/Menu.vue";
</script>

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

<script lang="ts">
export default {
  data() {
    return {
      activeSection: "general",
    };
  },
  methods: {
    setSection(section) {
      this.activeSection = section;
    },
  },
};
</script>

<style>
#profile-menu {
  align-self: baseline;
}
</style>
