import streamlit as st  
from PIL import Image
import requests



def load_image(image_file):
    image = Image.open(image_file)
    return image

def main():
    st.title('Recipe Idea Generator')

	
    # choice = st.sidebar.selectbox("Menu", menus)

    text_input = st.text_input("Enter current leftover ingredients in the fridge")
    
    # if choice == "Japchae":
    st.subheader("Recipe Ideas")
    # image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

    if text_input == "mushrooms":
        col1, col2 = st.columns(2)

        image = Image.open('1911_Japchae-Korean-Sweet-Potato-Noodles_550.jpeg')
        col1.header("Japchae")
        col1.image(image)
        #st.image(image, caption='Japchae')

        
        recipe = st.write("Make japcha at home if you want a comforting, delicious, and nutritionally balanced meal for your weekend dinner. The tender sweet potato noodles are tossed with charred beef and crispy veggies in a sweet savory sauce. This recipe uses shortcuts to make the cooking process easier than the traditional recipe.\n\n"
        "**Ingredients**\n\n"
        "serves 4\n\n"
        "- 4 ounces pork shoulder, cut into 1/4 inch wide and 2 1/2 inch long strips\n\n"
        "- 2 large dried shiitake mushrooms, soaked in warm water for 2 to 3 hours, cut into thin strips"
        "- 2 garlic cloves, minced\n\n"
        "- 1 tablespoons plus 2 teaspoons sugar\n\n"
        "- 2 tablespoons plus 1 teaspoon soy sauce\n\n"
        "- 2 tablespoons toasted sesame oil\n\n"
        "- 1 tablespoon toasted sesame seeds\n\n"
        "- 1 large egg\n\n"
        "- 4 ounces spinach, washed and drained\n\n"
        "- 4 ounces of dangmyeon (sweet potato starch noodles)\n\n"
        "- 2 to 3 green onions, cut crosswise into 2 inch long pieces\n\n"
        "- 1 medium onion (1 cup), sliced thinly\n\n"
        "- 4 to 5 white mushrooms, sliced thinly\n\n"
        "- 1 medium carrot (¾ cup), cut into matchsticks\n\n"
        "- ½ red bell pepper, cut into thin strips (optional)\n\n"
        "- ground black pepper\n\n"
        "- kosher salt\n\n"
        "- vegetable oil\n\n"
        "**Directions**\n\n"
        "Put the beef and shiitake mushrooms into a bowl and mix with 1 clove of minced garlic, 1 teaspoon sugar, ¼ teaspoon ground black pepper, 2 teaspoons soy sauce, and 1 teaspoon of toasted sesame oil with a wooden spoon or by hand. Cover and keep it in the fridge.\n\n"
        "Crack the egg and separate the egg yolk from the egg white. Remove the white stringy stuff (chalaza) from the yolk. Beat in a pinch of salt with a fork.\n\n"
        "Add 1 teaspoon of vegetable oil to a heated nonstick pan. Swirl the oil around so it covers the pan, and then wipe off the excess heated oil with a kitchen towel so only a thin layer remains on the pan.\n\n"
        "To keep the jidan as yellow as possible, turn off the heat and pour the egg yolk mixture into the pan. Tilt it around so the mixture spreads thinly. Let it cook using the remaining heat in the pan for about 1 minute. Flip it over and let it sit on the pan for 1 more minute.\n\n"
        "Let it cool and slice it into thin strips.\n\n"
        "Prepare the noodles and vegetables:\n\n"
        "Bring a large pot of water to a boil. Add the spinach and blanch for 30 seconds to 1 minute, then take it out with a slotted spoon or strainer. Let the water keep boiling to cook the noodles.\n\n"
        "Rinse the spinach in cold water to stop it from cooking. Squeeze it with your hands to remove any excess water. Cut it a few times and put it into a bowl. Mix with 1 teaspoon soy sauce and 1 teaspoon toasted sesame oil. Put it into a large mixing bowl.\n\n"
        "Put the noodles into the boiling water, cover and cook for 1 minute. Stir them with a wooden spoon so they don’t stick together. Cover and keep cooking for another 7 minutes until the noodles are soft and chewy.\n\n"
        "Strain and cut them a few times with kitchen scissors. Put the noodles into the large bowl next to the spinach. Add 2 teaspoons toasted sesame oil, 1 teaspoon soy sauce, and 1 teaspoon sugar. Mix well by hand or a wooden spoon. This process will season the noodles and also keep the noodles from sticking to each other.\n\n"
        "Heat up a skillet over medium high heat. Add 2 teaspoons vegetable oil with the onion, the green onion, and a pinch of salt. Stir-fry about 2 minutes until the onion looks a little translucent. Transfer to the noodle bowl.\n\n"
        "Heat up the skillet again and add 2 teaspoons vegetable oil. Add the white mushrooms and a pinch of salt. Stir-fry for 2 minutes until softened and a little juicy. Transfer to the noodle bowl.\n\n"
        "Heat up the skillet and add 1 teaspoon vegetable oil. Add the carrot and stir-fry for 20 seconds. Add the red bell pepper strips and stir-fry another 20 seconds. Transfer to the noodle bowl.\n\n"
        "Heat up the skillet and add 2 teaspoons vegetable oil. Add the beef and mushroom mixture and stir fry for a few minutes until the beef is no longer pink and the mushrooms are softened and shiny. Transfer to the noodle bowl.\n\n"
        "Mix and serve:\n\n"
        "Add 1 minced garlic clove, 1 tablespoon soy sauce, 1 tablespoon sugar, ½ teaspoon ground black pepper, and 2 teaspoons of toasted sesame oil to the mixing bowl full of ingredients. Mix all together by hand.\n\n"
        "Add the egg garnish and 1 tablespoon sesame seeds. Mix it and transfer it to a large plate and serve.\n\n")
        col2.header("Instructions")
        col2.write(recipe)
        
        col1, col2 = st.columns(2)
        imagetwo = Image.open('creamy miso mushroom pasta image.jpeg')
        col2.header("Creamy Miso Mushroom Pasta")
        col2.image(imagetwo)
        #st.image(image, caption='Creamy Miso Mushroom Pasta')
        recipetwo = st.write("**Ingredients**\n\n"
        "- 7 ounces dried pasta, such as bucatini\n\n"
        "- 4 ounces mushrooms (I use an equal mix of shimeji, eryngii, and oyster mushrooms, but most other combinations are good too)\n\n"
        "- 2 tablespoons vegetable oil\n\n" 
        "- 1 teaspoon sherry vinegar, or white wine vinegar\n\n"
        "- 2 teaspoons red miso paste\n\n"
        "- 3 tablespoons butter, softened\n\n"
        "- 5 garlic cloves\n\n"
        "- 1/2 cup heavy cream\n\n"
        "- 1 stalk of scallion, finely sliced\n\n"
        "- 1 pinch salt\n\n"
        "- 1 pinch black pepper\n\n"
        "**Directions**\n\n"
        "1. Bring a large pot of water to a rolling boil. Season generously with salt until it's nearly as salty as the sea, then add dried pasta. Cook the pasta until just under al dente (a minute less than on its package directions), then drain the pasta and set aside.\n\n"
        "2. Chop or pull apart the mushrooms into large, bite-sized chunks. Then, heat a large skillet over high heat with a tablespoon of vegetable oil, and sauté the mushrooms for 3-5 minutes until nicely browned. When they are done, add a little sherry vinegar to the pan with the mushrooms, give them a little toss, and set aside. It’s best to cook the mushrooms in 2-3 batches and not overcrowd the pan to allow them to brown evenly.\n\n"
        "3. To start on the sauce, whisk the red miso paste and butter together in a small bowl until it comes together to form a smooth, fluffy paste.\n\n"
        "4. In a medium saucepan, add the minced garlic and a tablespoon of oil, and stir-fry over medium heat for 30 seconds to a minute until fragrant. Add in the sautéed mushrooms. Then, add in the miso-butter mixture and cream, and bring this sauce to a boil, stirring gently. Finally, add the cooked pasta into the sauce, and stir until the pasta is well coated. Salt it to taste, and cook for 1-2 minutes until the pasta is al dente, then remove from the heat.\n\n"
        "5. Portion the pasta into two bowls, and top with sliced scallions and freshly cracked black pepper.")
        col1.header("Instructions")
        col1.write(recipetwo)


def main2():
    response = requests.get("http://localhost:8000/recipes")
    print('response: ', response.status_code)
    print('response: ', response.json())

    # requests.post()

    

if __name__ == '__main__':
    # main()
    main2()
