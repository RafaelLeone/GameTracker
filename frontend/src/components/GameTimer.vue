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
                    {{ horasJogadas }}
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
    props: {
        umJogoFoiAtualizado :{
            type: Number
        }
    },
    data () {
        return {
            total: '',
            restante: '',
            horasJogadas: ''
        }
    },
    methods: {
        calculoDeTimer(timer){
            this.total = timer.totalHours
            this.horasJogadas = timer.hoursPlayed
            this.restante = (timer.totalHours - timer.hoursPlayed)
            console.log(timer)
        },
        async inicializaDados(){
            const timer = await gamesApi.timer()
            this.calculoDeTimer(timer)
        }
    },
    async mounted() {
            await this.inicializaDados()
        },
    watch: {
        umJogoFoiAtualizado(){
         this.inicializaDados()   
        }
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