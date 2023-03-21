<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
        <game-list/>
    </v-responsive>
  </v-container>
</template>

<script>

import GameList from "@/components/GameList.vue"

export default {
  name: 'HomeView',
  components: {
    GameList
  }
}
</script>
