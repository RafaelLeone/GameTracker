<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
        <game-list @jogoAdicionado="onJogoAdicionado"/>
    </v-responsive>
  </v-container>
</template>

<script>
import GameForm from "@/components/GameForm.vue"
import GameList from "@/components/GameList.vue"
import { useAppStore } from "@/stores/appStore"

export default {
  name: 'HomeView',
  components: {
    GameForm,
    GameList,
  },
  data () {
    return{
      novoJogo: ''
    }
  },
  methods: {
    onJogoAdicionado (newGame) {
      this.novoJogo = newGame
      console.log("Recebi o evento")
    }
  }
}
</script>
