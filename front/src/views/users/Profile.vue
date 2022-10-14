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
import userAPI from "@/api/resources/users";
import { session } from "@/helpers/session";

const activeSection = ref("general");

onMounted(async () => {
  await userAPI
    .getUserFromEmail({ email: session.getEmail() })
    .then((response) => {
      const user = response.data;
      console.log(user);
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
