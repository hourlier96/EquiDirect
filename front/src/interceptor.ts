import axiosInstance from "./helpers/axios";
import { session } from "./helpers/session";
import { authStore } from "./stores/auth";
import router from "@/router/index";
import { notify } from "./helpers/notify";

const setup = () => {
  router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
      if (!session.isConnected()) {
        // Auth required, not connected
        next({ name: 'login' })
      } else {
        // Auth required, already connected
        next()
      }
    } else if (session.isConnected()) {
      // Not auth required, already connected
      next({ name: 'dashboard' })
    } else {
      // Not auth required, not connected
      next() 
    }
  })

  axiosInstance.axiosInstance.interceptors.request.use(
    (config) => {
      const store = authStore();
      // Send Bearer when user is connected
      if (store.accessToken) {
        const token = store.accessToken;
        if (config.headers) {
          config.headers["Authorization"] = `Bearer ${token}`;
          return config;
        }
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  axiosInstance.axiosInstance.interceptors.response.use(
    response => {
      if (response.status === 200 || response.status === 201) {
        return Promise.resolve(response);
      } else {
        return Promise.reject(response);
      }
    },
    error => {
      if (error.response.status) {
        switch (error.response.status) {
          case 401:
            notify.warning('Session expirée. Veuillez vous reconnecter.')
            authStore().$reset();
            router.push({
              path: "/login",
            });
            break;
          case 403:
            router.push({
              path: "/login",
            });
            break;
        }
        return Promise.reject(error.response);
      }
    }
  );
};

export default setup;
