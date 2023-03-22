<template>
    <div>
        <v-card
        class="cardzinho"
        width="400"
        prepend-icon="mdi-controller-classic"
      >
        <template v-slot:title>
          Planner Gamer
        </template>
    
        <v-card-text class="cardtext">
          <p>Total de horas em Games: {{ total }} </p>
          <p>Horas jogadas: {{ realizados }}</p>
          <p>Disponibilidade por semana: {{ disponibilidade }} </p>
          <p>Horas a cumprir por semana: {{ restante }} </p>
        </v-card-text>
      </v-card>
    </div>
</template>

<script>

import gamesApi from "@/api/games.api.js"

export default {
    data () {
        return {
            total: '',
            restante: '',
            disponibilidade: '',

        }
    },
    methods: {
        calculoDeTimer(timer){
            console.log(timer)
            this.total = timer.total
            this.realizados = timer.realizados
            this.restante = (timer.total - timer.realizados)
            this.disponibilidade = timer.disponibilidade
        }
    },
    mounted() {
            const timer = gamesApi.timer()
            this.calculoDeTimer(timer)
        }
}
</script>

<style>

.cardzinho{
    width: 400px;
    flex-direction: column;  

}

.v-card-item{
    grid-template-columns: none;
}

</style>