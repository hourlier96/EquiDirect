<script setup lang="ts">
import CardContainer from "./common/CardContainer.vue";
</script>

<template>
  <div class="dashboard">
    <div class="left-panel">
      <!-- <div class="row-dashboard">
        <q-card class="card-role">
          <q-img src="https://cdn.quasar.dev/img/parallax2.jpg">
            <div class="absolute-bottom text-h6">Les professionnels</div>
          </q-img>

          <q-card-section class="card-role-text">
            Entre en contact avec les entreprises qui te correspondent
          </q-card-section>
        </q-card>
        <q-card class="card-role">
          <q-img src="https://cdn.quasar.dev/img/parallax2.jpg">
            <div class="absolute-bottom text-h6">Les entreprises</div>
          </q-img>

          <q-card-section class="card-role-text">
            Trouve le candidat idéal à travers une sélection simple et intuitive
          </q-card-section>
        </q-card>
      </div> -->
    </div>
    <CardContainer>
      <q-carousel
        swipeable
        animated
        v-model="slide"
        :autoplay="autoplay"
        ref="carousel"
        infinite
      >
        <q-carousel-slide
          :name="1"
          img-src="https://cdn.quasar.dev/img/mountains.jpg"
        />
        <q-carousel-slide
          :name="2"
          img-src="https://cdn.quasar.dev/img/parallax1.jpg"
        />
        <q-carousel-slide
          :name="3"
          img-src="https://cdn.quasar.dev/img/parallax2.jpg"
        />
        <q-carousel-slide
          :name="4"
          img-src="https://cdn.quasar.dev/img/quasar.jpg"
        />

        <template v-slot:control>
          <q-carousel-control
            position="top-right"
            :offset="[18, 18]"
            class="text-white rounded-borders"
            style="background: rgba(0, 0, 0, 0.3); padding: 4px 8px"
          >
            <q-toggle
              dense
              dark
              color="orange"
              v-model="autoplay"
              label="Auto Play"
            />
          </q-carousel-control>

          <q-carousel-control
            position="bottom-right"
            :offset="[18, 18]"
            class="q-gutter-xs"
          >
            <q-btn
              push
              round
              dense
              color="orange"
              text-color="black"
              icon="arrow_left"
              @click="$refs.carousel.previous()"
            />
            <q-btn
              push
              round
              dense
              color="orange"
              text-color="black"
              icon="arrow_right"
              @click="$refs.carousel.next()"
            />
          </q-carousel-control>
        </template>
      </q-carousel>
    </CardContainer>
  </div>
</template>

<script lang="ts">
import { ref } from "vue";

export default {
  data() {
    return {
      slide: ref(1),
      autoplay: ref(true),
      lorem:
        "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Itaque voluptatem totam, architecto cupiditate officia rerum, error dignissimos praesentium libero ab nemo.",
    };
  },
};
</script>

<style>
.left-panel {
  width: 65%;
}

.row-dashboard {
  display: flex;
  justify-content: center;
  padding: 2rem;
}

.card-role {
  width: 100%;
  margin-right: 10px;
}

.card-role-text {
  text-align: center;
}
</style>
