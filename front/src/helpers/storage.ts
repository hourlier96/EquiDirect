import { watch } from "vue";
import defaultUser from "../stores/auth"

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
        const piniaState = JSON.parse((localStorage.getItem('piniaState') as string))
        if (!piniaState) {
            return {
                currentUser: defaultUser
            }
        }
        return piniaState.auth
    }
}