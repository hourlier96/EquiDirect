<template>
  <main>
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
const props = defineProps({
  register: Boolean,
});
</script>
