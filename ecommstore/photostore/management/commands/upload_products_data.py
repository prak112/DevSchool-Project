from django.core.management.base import BaseCommand
from photostore.models import Product


class Command(BaseCommand):
    help = "Upload images and their relevant information to the database"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Uploading image data..."))

        # DATA FORMAT  
    	# { "author": "AuthorName", "title": "ImageTitle", "description": "ImageDescription", "image_url": "https://www.example.com", "category": "ART", "theme": "LK", "image": 'images/image2.jpg', "status": "OOPS"},

        # "status":"OOPS" - viewable, NOT cart-able
        # "status":"AVL" - viewable AND cart-able

        # DATA (4 images/theme, 2original+2original-copy)
        image_data = [
            #PHOTOS
            # PH-Mountain
            {"author": "Daniel Handl", "title": "Twilight in the Mountains", "description": "Magnificent view of mountain peaks from above the clouds during sunset. Photo from Pexels by Daniel Handl from Pexels.", "image_url": "https://www.pexels.com/photo/snow-covered-mountain-under-blue-sky-3853501/", "category": "PH", "theme": "MT", "image": 'images/mountain-twilight.jpg', "status": "AVL"},
            {"author": "Daniel Handl", "title": "Twilight in the Mountains", "description": "Magnificent view of mountain peaks from above the clouds during sunset. Photo from Pexels by Daniel Handl from Pexels.", "image_url": "https://www.pexels.com/photo/snow-covered-mountain-under-blue-sky-3853501/", "category": "PH", "theme": "MT", "image": 'images/mountain-twilight.jpg', "status": "OOPS"},

            {"author": "Krivec Ales", "title": "Above All, We Stand", "description": "Magnificent view of mountain peaks from above the clouds during sunset. Photo from Pexels by Krivec Ales.", "image_url": "https://www.pexels.com/photo/gray-rock-mountain-547115/", "category": "PH", "theme": "MT", "image": 'images/mountain-above-clouds.jpg', "status": "AVL"},
            {"author": "Krivec Ales", "title": "Above All, We Stand", "description": "Magnificent view of mountain peaks from above the clouds during sunset. Photo from Pexels by Krivec Ales.", "image_url": "https://www.pexels.com/photo/gray-rock-mountain-547115/", "category": "PH", "theme": "MT", "image": 'images/mountain-above-clouds.jpg', "status": "OOPS"},

            ## PH-Lake
            {"author": "Quang Nguyen Vinh", "title": "Amidst the Fog, We See", "description": "A small island amidst the lake with foggy hills around. Photo from Pexels by Quang Nguyen Vinh.", "image_url": "https://www.pexels.com/photo/photo-of-body-of-water-2649403/", "category": "PH", "theme": "LK", "image": 'images/lake-foggy-hills.jpg', "status": "AVL"},
            {"author": "Quang Nguyen Vinh", "title": "Amidst the Fog, We See", "description": "A small island amidst the lake with foggy hills around. Photo from Pexels by Quang Nguyen Vinh.", "image_url": "https://www.pexels.com/photo/photo-of-body-of-water-2649403/", "category": "PH", "theme": "LK", "image": 'images/lake-foggy-hills.jpg', "status": "OOPS"},

            {"author": "Roman Pohorecki", "title": "Float with a View", "description": "Swimming with a wonderful view of the mountains around. Photo from Pexels by Roman Pohorecki.", "image_url": "https://www.pexels.com/photo/green-pine-trees-on-mountain-beside-the-body-of-water-15379/", "category": "PH", "theme": "LK", "image": 'images/lake-float-view.jpg', "status": "AVL"},
            {"author": "Roman Pohorecki", "title": "Float with a View", "description": "Swimming with a wonderful view of the mountains around. Photo from Pexels by Roman Pohorecki.", "image_url": "https://www.pexels.com/photo/green-pine-trees-on-mountain-beside-the-body-of-water-15379/", "category": "PH", "theme": "LK", "image": 'images/lake-float-view.jpg', "status": "OOPS"},

            ## PH-Polar
            {"author": "Frans van Heerden", "title": "Portal to the Heavens", "description": "The entrance to the Snow castle in the North Pole (Sodankylä, Finland) with a majestic presence of Aurora Borealis. Photo from Pexels by Frans van Heerden.", "image_url": "https://www.pexels.com/photo/aurora-borealis-624015/", "category": "PH", "theme": "PLR", "image": 'images/polar-snowcastle-aurora.jpg', "status": "OOPS"},
            {"author": "Frans van Heerden", "title": "Portal to the Heavens", "description": "The entrance to the Snow castle in the North Pole (Sodankylä, Finland) with a majestic presence of Aurora Borealis. Photo from Pexels by Frans van Heerden.", "image_url": "https://www.pexels.com/photo/aurora-borealis-624015/", "category": "PH", "theme": "PLR", "image": 'images/polar-snowcastle-aurora.jpg', "status": "AVL"},

            {"author": "Josy Mol", "title": "At Peace with Ice", "description": "A Weddell Seal posing for a photograph with a backdrop of the icy waters and the mountains. Photo from Pexels by Josy Mol.", "image_url": "https://www.pexels.com/photo/a-weddell-seal-in-close-up-photography-9695915/", "category": "PH", "theme": "PLR", "image": 'images/polar-seal-posing.jpg', "status": "OOPS"},
            {"author": "Josy Mol", "title": "At Peace with Ice", "description": "A Weddell Seal posing for a photograph with a backdrop of the icy waters and the mountains. Photo from Pexels by Josy Mol.", "image_url": "https://www.pexels.com/photo/a-weddell-seal-in-close-up-photography-9695915/", "category": "PH", "theme": "PLR", "image": 'images/polar-seal-posing.jpg', "status": "AVL"},

            ## PH-Forest
            {"author": "Arin Turkay", "title": "Wild River amidst Dense Forests", "description": "An aerial view of fast-flowing river between densely forested mountains. Photo from Pexels by Arin Turkay.", "image_url": "https://www.pexels.com/photo/aerial-photo-of-river-between-green-mountain-2591408/", "category": "PH", "theme": "FRST", "image": 'images/forest-aerial-view.jpg', "status": "OOPS"},
            {"author": "Arin Turkay", "title": "Wild River amidst Dense Forests", "description": "An aerial view of fast-flowing river between densely forested mountains. Photo from Pexels by Arin Turkay.", "image_url": "https://www.pexels.com/photo/aerial-photo-of-river-between-green-mountain-2591408/", "category": "PH", "theme": "FRST", "image": 'images/forest-aerial-view.jpg', "status": "AVL"},

            {"author": "Thomas P", "title": "Fog in the Woods", "description": "A relaxing sight of misty refreshment for anyone walking through this foggy forest. Photo from Pexels by Thomas P.", "image_url": "https://www.pexels.com/photo/fog-in-the-woods-15258289/", "category": "PH", "theme": "FRST", "image": 'images/forest-foggy-view.jpg', "status": "OOPS"},
            {"author": "Thomas P", "title": "Fog in the Woods", "description": "A relaxing sight of misty refreshment for anyone walking through this foggy forest. Photo from Pexels by Thomas P.", "image_url": "https://www.pexels.com/photo/fog-in-the-woods-15258289/", "category": "PH", "theme": "FRST", "image": 'images/forest-foggy-view.jpg', "status": "AVL"},

            ## PH-Tree
            {"author": "Jack Redgate", "title": "On Top of the World", "description": "A lone standing tree on top of the mountain. Photo from Pexels by Jack Redgate.", "image_url": "https://www.pexels.com/photo/tree-on-top-of-a-mountain-3049337/", "category": "PH", "theme": "TR", "image": 'images/tree-standing-tall.jpg', "status": "AVL"},
            {"author": "Jack Redgate", "title": "On Top of the World", "description": "A lone standing tree on top of the mountain. Photo from Pexels by Jack Redgate.", "image_url": "https://www.pexels.com/photo/tree-on-top-of-a-mountain-3049337/", "category": "PH", "theme": "TR", "image": 'images/tree-standing-tall.jpg', "status": "OOPS"},

            {"author": "Yan Krukau", "title": "The Gentle Giant", "description": "An arched banyan tree (probably) made way through its roots to allow passage. Photo from Pexels by Yan Krukau.", "image_url": "https://www.pexels.com/photo/arch-from-old-tree-in-park-5479852/", "category": "PH", "theme": "TR", "image": 'images/tree-making-way.jpg', "status": "AVL"},
            {"author": "Yan Krukau", "title": "The Gentle Giant", "description": "An arched banyan tree (probably) made way through its roots to allow passage. Photo from Pexels by Yan Krukau.", "image_url": "https://www.pexels.com/photo/arch-from-old-tree-in-park-5479852/", "category": "PH", "theme": "TR", "image": 'images/tree-making-way.jpg', "status": "OOPS"},

            ## PH-Flower
            {"author": "Gilberto Olimpio", "title": "Alien Flower", "description": "Blue lily or famously known as the Lily-of-the-Nile, widely present in the tropical region. Photo from Pexels by Gilberto Olimpio.", "image_url": "https://www.pexels.com/photo/close-up-photo-of-blue-flower-3686216/", "category": "PH", "theme": "FLWR", "image": 'images/flower-blue-lily.jpg', "status": "OOPS"},
            {"author": "Gilberto Olimpio", "title": "Alien Flower", "description": "Blue lily or famously known as the Lily-of-the-Nile, widely present in the tropical region. Photo from Pexels by Gilberto Olimpio.", "image_url": "https://www.pexels.com/photo/close-up-photo-of-blue-flower-3686216/", "category": "PH", "theme": "FLWR", "image": 'images/flower-blue-lily.jpg', "status": "AVL"},

            {"author": "Hiếu Hoàng", "title": "Flame of the Forest", "description": "Royal Poinciana and many other interesting names based on its location of existence in the tropics, one of them is Peacock Flower. Photo from Pexels by Hiếu Hoàng.", "image_url": "https://www.pexels.com/photo/tilt-shift-lens-of-green-plants-668465/", "category": "PH", "theme": "FLWR", "image": 'images/flower-gold-mohar.jpg', "status": "OOPS"},
            {"author": "Hiếu Hoàng", "title": "Flame of the Forest", "description": "Royal Poinciana and many other interesting names based on its location of existence in the tropics, one of them is Peacock Flower. Photo from Pexels by Hiếu Hoàng.", "image_url": "https://www.pexels.com/photo/tilt-shift-lens-of-green-plants-668465/", "category": "PH", "theme": "FLWR", "image": 'images/flower-gold-mohar.jpg', "status": "AVL"},

            #ART
            ## ART-Mountain
            {"author": "Bing Image Creator", "title": "Mountain sunrise view", "description": "An AI generated pencil drawing of a mountain sunrise view. Image Generated with AI on November 15, 2023 at 8:24 PM.", "image_url": "https://www.bing.com/images/create/sunrise-mountain-view-pencil-drawing/65550cbfa35e493fa503e13426ab5688?id=4TjrvaHzTvjPuN3cf3Vj4g%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "MT", "image": 'images/mountain-sunrise-view.jpg', "status": "OOPS"},
            {"author": "Bing Image Creator", "title": "Mountain sunrise view", "description": "An AI generated pencil drawing of a mountain sunrise view. Image Generated with AI on November 15, 2023 at 8:24 PM.", "image_url": "https://www.bing.com/images/create/sunrise-mountain-view-pencil-drawing/65550cbfa35e493fa503e13426ab5688?id=4TjrvaHzTvjPuN3cf3Vj4g%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "MT", "image": 'images/mountain-sunrise-view.jpg', "status": "AVL"},

        	{"author": "Bing Image Creator", "title": "Mountain seaside view", "description": "An AI generated pencil drawing of a mountain seaside view. Image Generated with AI on November 15, 2023 at 8:24 PM.", "image_url": "https://www.bing.com/images/create/seaside-mountain-view-similar-to-cornwall-coast-pe/65550d8e121f463dbb9cf79b4b51afe3?id=LUdOIBBby6ApXTvaRCp%2fuA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "MT", "image": 'images/mountain-seaside-view.jpg', "status": "OOPS"},
        	{"author": "Bing Image Creator", "title": "Mountain seaside view", "description": "An AI generated pencil drawing of a mountain seaside view. Image Generated with AI on November 15, 2023 at 8:24 PM.", "image_url": "https://www.bing.com/images/create/seaside-mountain-view-similar-to-cornwall-coast-pe/65550d8e121f463dbb9cf79b4b51afe3?id=LUdOIBBby6ApXTvaRCp%2fuA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "MT", "image": 'images/mountain-seaside-view.jpg', "status": "AVL"},

            ## ART-Lake
            {"author": "Bing Image Creator", "title": "Lakeside village port", "description": "An AI generated pencil drawing of a lakeside village at the portside. Image Generated with AI on November 15, 2023 at 7:59 PM.", "image_url": "https://www.bing.com/images/create/lakeside-village-pencil-drawing/65550704f9984773aecb3ee17ccd4ae1?id=Bh3RdxoU0shiWzIuzWU72Q%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "LK", "image": 'images/lake-lakeside-village.jpg', "status": "AVL"},
            {"author": "Bing Image Creator", "title": "Lakeside village port", "description": "An AI generated pencil drawing of a lakeside village at the portside. Image Generated with AI on November 15, 2023 at 7:59 PM.", "image_url": "https://www.bing.com/images/create/lakeside-village-pencil-drawing/65550704f9984773aecb3ee17ccd4ae1?id=Bh3RdxoU0shiWzIuzWU72Q%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "LK", "image": 'images/lake-lakeside-village.jpg', "status": "OOPS"},

            {"author": "Bing Image Creator", "title": "Isolated Lake view", "description": "An AI generated pencil drawing of an isolated lake with an island of trees. Image Generated with AI on November 15, 2023 at 7:59 PM.", "image_url": "https://www.bing.com/images/create/isolated-lake-view-pencil-drawing/6555085e62d44a8eb0c524c660ca28f0?id=x2yLfse4KKkSgNlxlDkNZA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "LK", "image": 'images/lake-isolated-view.jpg', "status": "AVL"},
            {"author": "Bing Image Creator", "title": "Isolated Lake view", "description": "An AI generated pencil drawing of an isolated lake with an island of trees. Image Generated with AI on November 15, 2023 at 7:59 PM.", "image_url": "https://www.bing.com/images/create/isolated-lake-view-pencil-drawing/6555085e62d44a8eb0c524c660ca28f0?id=x2yLfse4KKkSgNlxlDkNZA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "LK", "image": 'images/lake-isolated-view.jpg', "status": "OOPS"},

            ## ART-Polar
            {"author": "Bing Image Creator", "title": "Frozen Waterfalls", "description": "An AI generated pencil drawing of frozen waterfalls. Image Generated with AI on November 15, 2023 at 8:08 PM.", "image_url": "https://www.bing.com/images/create/frozen-waterfall-pencil-drawing/6555090772584e39bcf607664037708a?id=tUwhFNi4XwG7P9hd4n%2buxA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "PLR", "image": 'images/polar-frozen-waterfall.jpg', "status": "AVL"},
            {"author": "Bing Image Creator", "title": "Frozen Waterfalls", "description": "An AI generated pencil drawing of frozen waterfalls. Image Generated with AI on November 15, 2023 at 8:08 PM.", "image_url": "https://www.bing.com/images/create/frozen-waterfall-pencil-drawing/6555090772584e39bcf607664037708a?id=tUwhFNi4XwG7P9hd4n%2buxA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "PLR", "image": 'images/polar-frozen-waterfall.jpg', "status": "OOPS"},

            {"author": "Bing Image Creator", "title": "Frozen Lake", "description": "An AI generated pencil drawing of a frozen lake with a background of forest and mountains. Image Generated with AI on November 15, 2023 at 8:08 PM.", "image_url": "https://www.bing.com/images/create/transparent-frozen-lake-pencil-drawing/6555099936154a0b9ff54b5fe7686a90?id=j6mTJe64s9bazaZi45Th6g%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "PLR", "image": 'images/polar-frozen-lake.jpg', "status": "AVL"},
            {"author": "Bing Image Creator", "title": "Frozen Lake", "description": "An AI generated pencil drawing of a frozen lake with a background of forest and mountains. Image Generated with AI on November 15, 2023 at 8:08 PM.", "image_url": "https://www.bing.com/images/create/transparent-frozen-lake-pencil-drawing/6555099936154a0b9ff54b5fe7686a90?id=j6mTJe64s9bazaZi45Th6g%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "PLR", "image": 'images/polar-frozen-lake.jpg', "status": "OOPS"},

            ## ART-Forest
            {"author": "Bing Image Creator", "title": "Sunlit path in the Forest", "description": "An AI generated pencil drawing of sunlit path inside the forest. Image Generated with AI on November 15, 2023 at 8:16 PM.", "image_url": "https://www.bing.com/images/create/path-through-a-forest-with-sunlight-at-the-end-of-/65550a3adf9444288aa55f825ab5d148?id=wl5YmtjagUtnNKH1nxqt%2bg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FRST", "image": 'images/forest-path-sunlight.jpg', "status": "AVL"},
            {"author": "Bing Image Creator", "title": "Sunlit path in the Forest", "description": "An AI generated pencil drawing of sunlit path inside the forest. Image Generated with AI on November 15, 2023 at 8:16 PM.", "image_url": "https://www.bing.com/images/create/path-through-a-forest-with-sunlight-at-the-end-of-/65550a3adf9444288aa55f825ab5d148?id=wl5YmtjagUtnNKH1nxqt%2bg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FRST", "image": 'images/forest-path-sunlight.jpg', "status": "OOPS"},

            {"author": "Bing Image Creator", "title": "Foggy Tropical Forest", "description": "An AI generated pencil drawing of a foggy tropical forest with a trailing path. Image Generated with AI on November 15, 2023 at 8:16 PM.", "image_url": "https://www.bing.com/images/create/deciduous-forest-in-the-tropics-with-fog-pencil-dr/65550b06279d4e02abcb798313f4c3a5?id=tpHQbnpXxeT0LaS0FePpaA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FRST", "image": 'images/forest-tropical-foggy.jpg', "status": "AVL"},
            {"author": "Bing Image Creator", "title": "Foggy Tropical Forest", "description": "An AI generated pencil drawing of a foggy tropical forest with a trailing path. Image Generated with AI on November 15, 2023 at 8:16 PM.", "image_url": "https://www.bing.com/images/create/deciduous-forest-in-the-tropics-with-fog-pencil-dr/65550b06279d4e02abcb798313f4c3a5?id=tpHQbnpXxeT0LaS0FePpaA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FRST", "image": 'images/forest-tropical-foggy.jpg', "status": "OOPS"},

            ## ART-Tree
            {"author": "Bing Image Creator", "title": "Strong Roots", "description": "An AI generated pencil drawing of a decidious tree at the edge of a lake with its roots spreading beautifully. Image Generated with AI on November 15, 2023 at 8:33 PM.", "image_url": "https://www.bing.com/images/create/deciduous-tree-in-a-rainforest-with-lake-around-pe/65550e6f7eee4f34853f834829499339?id=Sz2RoQzAHbzxuwS%2fkibPpQ%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "TR", "image": 'images/tree-decidious-rainforest.jpg', "status": "OOPS"},
            {"author": "Bing Image Creator", "title": "Strong Roots", "description": "An AI generated pencil drawing of a decidious tree at the edge of a lake with its roots spreading beautifully. Image Generated with AI on November 15, 2023 at 8:33 PM.", "image_url": "https://www.bing.com/images/create/deciduous-tree-in-a-rainforest-with-lake-around-pe/65550e6f7eee4f34853f834829499339?id=Sz2RoQzAHbzxuwS%2fkibPpQ%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "TR", "image": 'images/tree-decidious-rainforest.jpg', "status": "AVL"},

            {"author": "Bing Image Creator", "title": "Chilling in the Snow", "description": "An AI generated pencil drawing of Pine trees hibernating for the winter under the snow. Image Generated with AI on November 15, 2023 at 8:33 PM.", "image_url": "https://www.bing.com/images/create/pine-tree-under-snow-fall-pencil-drawing/65550ed56a3647a79972878371ed3c4b?id=UfDwU%2fK9H3V2UXoIUyQcLg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "TR", "image": 'images/tree-pine-snowfall.jpg', "status": "OOPS"},
            {"author": "Bing Image Creator", "title": "Chilling in the Snow", "description": "An AI generated pencil drawing of Pine trees hibernating for the winter under the snow. Image Generated with AI on November 15, 2023 at 8:33 PM.", "image_url": "https://www.bing.com/images/create/pine-tree-under-snow-fall-pencil-drawing/65550ed56a3647a79972878371ed3c4b?id=UfDwU%2fK9H3V2UXoIUyQcLg%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "TR", "image": 'images/tree-pine-snowfall.jpg', "status": "AVL"},

            ## ART-Flower
            {"author": "Bing Image Creator", "title": "Blossoming Flowers", "description": "An AI generated pencil drawing of blossoming flowers. Image Generated with AI on November 15, 2023 at 8:42 PM.", "image_url": "https://www.bing.com/images/create/flowers-blossoming-pencil-drawing/65550f66e9c840e890defa4805987052?id=DUgaK8NoB%2b8XTGv1cV88KQ%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FLWR", "image": 'images/flower-blossom.jpg', "status": "OOPS"},
            {"author": "Bing Image Creator", "title": "Blossoming Flowers", "description": "An AI generated pencil drawing of blossoming flowers. Image Generated with AI on November 15, 2023 at 8:42 PM.", "image_url": "https://www.bing.com/images/create/flowers-blossoming-pencil-drawing/65550f66e9c840e890defa4805987052?id=DUgaK8NoB%2b8XTGv1cV88KQ%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FLWR", "image": 'images/flower-blossom.jpg', "status": "AVL"},

            {"author": "Bing Image Creator", "title": "Forest Flame releasing pollen", "description": "An AI generated pencil drawing of royal poinciana releasing pollen. Image Generated with AI on November 15, 2023 at 8:42 PM.", "image_url": "https://www.bing.com/images/create/royal-poinciana-flower-releasing-pollen-with-tree-/655510e6da7b4323a2df1ddaa28ce2a9?id=Z0ipR0kTQi4j6%2fbS4iYMTA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FLWR", "image": 'images/flower-poinciana-pollen.jpg', "status": "OOPS"},
            {"author": "Bing Image Creator", "title": "Forest Flame releasing pollen", "description": "An AI generated pencil drawing of royal poinciana releasing pollen. Image Generated with AI on November 15, 2023 at 8:42 PM.", "image_url": "https://www.bing.com/images/create/royal-poinciana-flower-releasing-pollen-with-tree-/655510e6da7b4323a2df1ddaa28ce2a9?id=Z0ipR0kTQi4j6%2fbS4iYMTA%3d%3d&view=detailv2&idpp=genimg&idpclose=1&FORM=SYDBIC", "category": "ART", "theme": "FLWR", "image": 'images/flower-poinciana-pollen.jpg', "status": "AVL"},
        ]


        # create 'Product' instances and upload to database
        product_instances = [Product(**data) for data in image_data]
        Product.objects.bulk_create(product_instances)

        self.stdout.write(self.style.SUCCESS("Image upload complete!"))
