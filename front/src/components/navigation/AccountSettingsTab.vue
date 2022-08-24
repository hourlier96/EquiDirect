<template>
  <q-btn flat color="green" label="Profil">
    <q-menu>
      <div class="row no-wrap q-pa-md">
        <div class="column">
          <div class="username text-h6 q-mb-md">John Doe</div>
          <q-separator class="q-mx-lg" />
          <q-btn class="see-profil-btn" color="green" push size="sm">
            Voir mon profil
          </q-btn>
        </div>

        <q-separator vertical inset class="q-mx-lg" />

        <div class="column items-center">
          <q-avatar class="pic-profil" size="72px">
            <img src="https://cdn.quasar.dev/img/avatar4.jpg" />
          </q-avatar>
          <div>
            <q-btn color="red" label="Logout" push size="sm" v-close-popup />
          </div>
        </div>
      </div>
    </q-menu>
  </q-btn>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    return {
      mobileData: ref(true),
      bluetooth: ref(false),
    };
  },
};
</script>

<style>
.pic-profil,
.username {
  margin-bottom: auto;
}

.see-profil-btn {
  margin-top: auto;
}
</style>
