import { watch } from "vue";

export const storage = {
    syncStoreWithLocalStorage(pinia: any) {
        watch(
            pinia.state,
            (state) => {
                // persist the whole state to the local storage whenever it changes
                localStorage.setItem("piniaState", JSON.stringify(state));
                // console.log('Sync', localStorage.getItem('piniaState'))
            },
            { deep: true }
        );
    },

    getAuth() {
        return JSON.parse((localStorage.getItem('piniaState') as string)).auth
    }
}