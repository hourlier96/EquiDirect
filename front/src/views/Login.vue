<template>
  <main>
    <RegisterForm v-if="props.register" id="register-form" />
    <LoginForm v-else id="login-form" />
  </main>
</template>

<script setup lang="ts">
import RegisterForm from "@/components/auth/RegisterForm.vue";
import LoginForm from "@/components/auth/LoginForm.vue";
const props = defineProps({
  register: Boolean,
});
</script>

<style>
#login-form,
#register-form {
  margin: auto;
}
</style>
