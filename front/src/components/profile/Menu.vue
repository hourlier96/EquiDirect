<template>
  <CardContainer class="col-3 q-mr-lg">
    <q-list bordered>
      <div v-for="(item, index) in items">
        <q-item
          :active="isActive(item.name)"
          active-class="text-white bg-green"
          :to="`${session.getRole().toLowerCase()}?view=${item.name}`"
          clickable
          v-ripple
          @click="setActiveSection(item.name)"
        >
          <q-item-section avatar>
            <q-icon color="black" :name="item.icon" />
          </q-item-section>
          <q-item-section>{{ item.label }}</q-item-section>
        </q-item>
        <q-separator v-if="index < items.length - 1" />
      </div>
    </q-list>
  </CardContainer>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { session } from "@/helpers/session";
import CardContainer from "@/components/common/CardContainer.vue";

const props = defineProps({
  activeSection: { type: String, default: "general" },
});

const emit = defineEmits(["setActiveSection"]);

const items = ref([
  {
    name: "general",
    icon: "account_circle",
    label: "Informations générales",
  },
  {
    name: "skills",
    icon: "fas fa-chess-knight",
    label: "Compétences",
  },
  {
    name: "search",
    icon: "search",
    label: "Critères de recherche",
  },
]);

function isActive(section) {
  return props.activeSection == section;
}

function setActiveSection(section) {
  emit("setActiveSection", section);
}
</script>
