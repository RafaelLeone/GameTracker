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
            <v-row>
                <v-col>
                    Total de horas em Games
                </v-col>
                <v-col>
                    {{ total }} 
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    Horas jogadas
                </v-col>
                <v-col>
                    {{ realizados }}
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    Horas faltantes
                </v-col>
                <v-col>
                    {{ restante }}
                </v-col>
            </v-row>
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
            realizados: ''

        }
    },
    methods: {
        calculoDeTimer(timer){
            console.log(timer)
            this.total = timer.total
            this.realizados = timer.realizados
            this.restante = (timer.total - timer.realizados)
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

.v-row{
    text-align: -webkit-center
}

.v-col{
    padding: 2%
}

</style>