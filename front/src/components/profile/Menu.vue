<script setup lang="ts">
import CardContainer from "@/components/common/CardContainer.vue";
import { session } from "@/helpers/session";
</script>

<template>
  <CardContainer class="col-3 q-mr-lg">
    <q-list bordered>
      <q-item
        :active="isActive('general')"
        active-class="text-white bg-green"
        :to="`${session.getRole().toLowerCase()}?view=general`"
        clickable
        v-ripple
        @click="setActiveSection('general')"
      >
        <q-item-section avatar>
          <q-icon color="black" name="account_circle" />
        </q-item-section>
        <q-item-section>Informations générales</q-item-section>
      </q-item>
      <q-separator />
      <q-item
        :active="isActive('skills')"
        active-class="text-white bg-green"
        :to="`${session.getRole().toLowerCase()}?view=skills`"
        clickable
        v-ripple
        @click="setActiveSection('skills')"
      >
        <q-item-section avatar>
          <q-icon color="black" name="fas fa-chess-knight" />
        </q-item-section>
        <q-item-section>Compétences</q-item-section>
      </q-item>
      <q-separator />
      <q-item
        :active="isActive('search')"
        active-class="text-white bg-green"
        :to="`${session.getRole().toLowerCase()}?view=search`"
        clickable
        v-ripple
        @click="setActiveSection('search')"
      >
        <q-item-section avatar>
          <q-icon color="black" name="search" />
        </q-item-section>
        <q-item-section>Critères de recherche </q-item-section>
      </q-item>
    </q-list>
  </CardContainer>
</template>

<script lang="ts">
export default {
  props: {
    activeSection: {
      type: String,
      default: "general",
    },
  },
  methods: {
    isActive(section) {
      return this.activeSection == section;
    },
    setActiveSection(section) {
      this.$emit("setActiveSection", section);
    },
  },
};
</script>
