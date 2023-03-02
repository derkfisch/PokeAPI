class PokemonAPI:
    base_url = "'https://pokeapi.co/ap1/v2/"
    
    def get__(self):
        poke_res = requests.get(f"{self.base_url}pokemon/ditto.json")
        if poke_res.ok:
            return poke_res.json()
    
    def get_attr(self, ditto):
        data = self.get__(ditto)
        ditto_weight = data['abilities']['weight']
        ditto_height = data['abilities']['height']
                
print(data.get("abilities"))
print(f"{ditto}.title() weighs {ditto_weight} and is {ditto_height} inches tall)")