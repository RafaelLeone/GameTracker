<template>
  <VLayout>
    <app-error-dialog :show="showErrorMessage" :message="errorMessage" @close="closeErrorDialog" />
    <app-snackbar />
    <v-app :theme="theme">
      <app-nav-bar :theme="theme" @theme-click="onThemeClick"></app-nav-bar>
      <RouterView />
      <game-player v-if="gameRow.length" class="p-5" :songs="gameRow" @close-player="clearGames"></game-player>
    </v-app>
  </VLayout>
</template>

<script setup>
import { ref } from "vue"
import { useGameStore } from "@/stores/gameStore"

const theme = ref("dark")

function onThemeClick() {
  theme.value = theme.value === "light" ? "dark" : "light"
}
</script>

<script>
import { mapState } from "pinia"
import { useAppStore } from "@/stores/appStore"
import { useAccountsStore } from "@/stores/accountsStore"
import AppSnackbar from "@/components/AppSnackbar.vue"
import AppErrorDialog from "@/components/AppErrorDialog.vue"
import AppNavBar from "@/components/AppNavBar.vue"

export default {
  name: "DefaultLayout",
  components: {
    AppSnackbar,
    AppErrorDialog,
    AppNavBar,
  },
  setup() {
    const appStore = useAppStore()
    const gameStore = useGameStore()
    return { appStore, gameStore }
  },
  computed: {
    ...mapState(useAppStore, ["errorMessage", "showErrorMessage"]),
    ...mapState(useAccountsStore, ["loggedUser"]),
    ...mapState(useGameStore, ["gameRow"]),
  },
  methods: {
    closeErrorDialog() {
      this.appStore.setShowErrorMessage(null)
    },
    clearGames () {
      this.gameStore.clearRow()
    }
  },
}
</script>
