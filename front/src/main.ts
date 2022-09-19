import { createApp } from "vue";
import { createPinia } from "pinia";

import { Quasar } from "quasar";
import quasarLang from "quasar/lang/fr";

// Import icon libraries
import "@quasar/extras/material-icons/material-icons.css";

// Import Quasar css
import "quasar/src/css/index.sass";
import "quasar/src/css/flex-addon.sass"
import { Notify } from "quasar";

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);

app.use(Quasar, {
  plugins: {Notify}, // import Quasar plugins and add here
  lang: quasarLang,
});

app.use(createPinia());
app.use(router);

app.mount("#app");
