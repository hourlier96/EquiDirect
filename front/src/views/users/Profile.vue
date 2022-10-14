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
import { ref, onMounted } from "vue";
import Menu from "@/components/profile/Menu.vue";
import individualAPI from "@/api/resources/individual";
import { session } from "@/helpers/session";

const activeSection = ref("general");

onMounted(async () => {
  await individualAPI
    .getIndividualFromUser({ user_id: session.getId() })
    .then((response) => {
      const individual = response.data;
      console.log(individual);
    });
});

function setSection(section) {
  activeSection.value = section;
}
</script>

<style>
#profile-menu {
  align-self: baseline;
}
</style>
