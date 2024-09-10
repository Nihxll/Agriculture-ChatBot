def information(agricultural_info):
    agriculture = {
         'wheat' : [

      ' * TEMPARATURE          : Thrives in cooler climates with moderate temperatures.\n'
      ' * GRAINS               : Produces edible grains used in various food products like bread, pasta, and cereal.\n'
      ' * RUST-RESISTANT       : Some wheat varieties are bred to resist common fungal diseases like wheat rust.\n'
      ' * HESSIAN-FLY TOLERANT : Certain wheat cultivars possess tolerance or resistance to the Hessian fly, a common pest.\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Wheat \n'
'\nType thank you to end this conversation\n' 
    ],
         'rice' :[

      ' * FLODDED         : Rice fields are often flooded to control weeds and provide the anaerobic conditions necessary for growth.\n'
      ' * PADDIES         : Rice is commonly cultivated in flooded fields known as paddies.\n'
      ' * STAPLE          : A staple food for a large portion of the worlds population, especially in Asia.\n'
      ' * BLAST-RESISTANT : Certain rice varieties are bred to resist rice blast, a devastating fungal disease.\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Rice \n'
'\nType thank you to end this conversation\n' 
    ],
         'corn' :[

      ' * VERSATILE CROP   : Corn is used in various forms, including food for humans and animals, biofuel, and industrial products.\n'
      ' * POLLINATION      : Corn relies on wind pollination, making proper spacing essential for optimal yield.\n'
      ' * HYBRID           : Many modern corn varieties are hybrids, bred for specific traits such as high yield or pest resistance.\n' 
      ' * DROUGHT-TOLERANT : Some corn hybrids are bred to withstand drought conditions, which can be crucial in areas with erratic rainfall.\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Maize \n'
'\nType thank you to end this conversation\n'     
    ],
         'soybeans' :[

      ' * LEGUME          : Belongs to the legume family and can fix atmospheric nitrogen, enriching the soil.\n'
      ' * NITROGEN-FIXING : Soybeans have a symbiotic relationship with nitrogen-fixing bacteria, reducing the need for nitrogen fertilizers.\n'
      ' * OILSEEDS        : Soybeans are a significant source of vegetable oil used in cooking, biodiesel production, and various industrial applications.\n'
      ' * PROTEIN-RICH    : Soybeans are an excellent source of plant-based protein, used in food products like tofu, soy milk, and meat substitutes.\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Soybean \n'
'\nType thank you to end this conversation\n' 
    ],

         'cotton' :[

      ' * FIBER    : Cotton is primarily cultivated for its soft, fluffy fibers, which are spun into yarn and woven into textiles.\n'
      ' * LINT     : The cotton fiber, also known as lint, is harvested from cotton bolls after the seeds are removed.\n'
      ' * GOSSYPOL : A natural toxin found in cotton plants, which serves as a defense mechanism against pests.\n'
      ' * GIN      : The cotton gin is a machine used to separate cotton fibers from the seeds, revolutionizing cotton production in the 18th century.\n '
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Cotton \n'
'\nType thank you to end this conversation\n'    
    ],
         'potatoe' :[

      ' * VERSATILE CROP     : Potatoes are highly versatile root vegetables cultivated worldwide for their edible tubers.\n'
      ' * GROWING CONDITIONS : They thrive in cool climates with well-drained, sandy soil and full sun.\n'
      ' * HARVESTING         : Done when foliage dies back, typically in late summer or fall.\n'
      ' * PLANTING           : Usually done in early spring at a depth of about 4 inches (10 cm).\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Potato \n'
'\nType thank you to end this conversation\n'      
    ],
         'tomato' :[
             
      ' * CROP TYPE          : Tomatoes are fruit-bearing plants cultivated for their edible fruits, which are used as vegetables in cooking.\n'
      ' * GROWING CONDITIONS : Tomatoes thrive in warm climates with plenty of sunlight.They require well-drained soil with good fertility and consistent moisture.\n'
      ' * PLANTING           : Seedlings are transplanted into the garden after the danger of frost has passed.They should be planted deeply for strong root development.\n' 
      ' * HARVESTING         : Tomatoes are typically harvested when they reach full color and firmness.They should be picked carefully to avoid bruising and stored at room temperature to ripen fully.\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Tomato \n' 
'\nType thank you to end this conversation\n'   
    ],
         'sugarcane' :[
             
       ' * CROP TYPE          : Sugarcane is a tall perennial grass cultivated for its high sugar content in its stalks.\n'
       ' * PROPAGATION        : Sugarcane is propagated through stem cuttings known as setts, which are planted horizontally in furrows or trenches.\n'
       ' * GROWING CONDITIONS : Sugarcane thrives in tropical and subtropical climates with warm temperatures, ample sunlight, and well-drained soil.\n'
       ' * CROP ROTATION      : Crop rotation is often practiced in sugarcane cultivation to manage soil fertility and reduce pest and disease pressure. Common rotation crops include legumes and cereals.\n' 
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Sugarcane \n'   
'\nType thank you to end this conversation\n' 
   ],
         'coffee' :[

       ' * GROWING CONDITIONS : Coffee plants thrive in tropical climates with well-drained soil,altitudes ranging from 600 to 2000 meters,and temperatures between 15°C to 24°C.\n' 
       ' * PLANTING           : Coffee seeds or seedlings are planted in shaded nurseries before being transplanted to the field.\n' 
       ' * GROWTH CYCLE       : Coffee plants go through stages including flowering,fruit development,and harvesting.They typically begin producing beans in their third or fourth year.\n'
       ' * HARVESTING         : Coffee cherries are hand-picked when they reach peak ripeness, usually once or twice a year depending on the region and variety.\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Coffee \n'       
'\nType thank you to end this conversation\n' 
    ],
         'barley' :[

       ' * CROP TYPE          : Barley is a cereal grain cultivated for its seeds, known as barley kernels or barley grains.\n'
       ' * PLANTING           : Barley is sown in the fall for winter barley or in the spring for summer barley, depending on the climate and variety.\n' 
       ' * GROWING CONDITIONS : Barley thrives in temperate climates with well-drained soil and moderate rainfall. It can tolerate cooler temperatures better than other cereal grains.\n'
       ' * GROWTH CYCLE       : Barley undergoes stages of germination, tillering (development of side shoots), stem elongation, flowering, grain filling, and ripening.\n'
'\nFOR MORE INFORMATION VISIT : https://en.wikipedia.org/wiki/Barley \n'
'\nType thank you to end this conversation\n'         
    ], 
        
    }

    return agriculture.get(agricultural_info)