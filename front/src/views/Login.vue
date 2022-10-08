<template>
  <main>
    <img
      v-if="!session.isConnected()"
      class="logo q-mx-auto q-mb-md"
      src="src/assets/images/logo.png"
      alt="Equisphere"
    />
    <RegisterForm
      v-if="props.register"
      id="register-form"
      class="q-mx-auto q-my-auto"
    />
    <LoginForm v-else id="login-form" class="q-mx-auto q-my-auto" />
  </main>
</template>

<script setup lang="ts">
import RegisterForm from "@/components/auth/RegisterForm.vue";
import LoginForm from "@/components/auth/LoginForm.vue";
import { session } from "@/helpers/session";
const props = defineProps({
  register: Boolean,
});
</script>

<style>
.logo {
  display: block;
}
</style>
