# Circle ZigZag dataset

This repository has a very tiny image dataset of hand drawing of Circle and ZigZag.
In addition, it has datasets including more classes like 5 and 41 classes.

* Number of classes is 2. (and 5, 41.)
* Image size is 28x28. 
* 6000 images for each classes.

You can download dataset as follows.

```
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/2/train.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/2/test.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/2/answer.csv
```

`train.zip` is dataset for training.
`test.zip` is dataset for testing.
`answer.csv` is answers of testing.

If you would like to get class list from training images, you can get them as follows.

```python
images = os.listdir("./train")
class_list = sorted(list(set([f.split("_")[0] for f in images])))
```

## 2 classes dataset

* Classes: circle and zigzag

```
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/2/train.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/2/test.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/2/answer.csv
```

example:

class|-|-
-|-|-
circle|![circle_4](https://user-images.githubusercontent.com/329257/37872317-2e853670-3040-11e8-9d87-76c723297c3f.jpg)|![circle_467](https://user-images.githubusercontent.com/329257/37872318-34a05b7a-3040-11e8-8419-18829de593e0.jpg)
zigzag|![zigzag_5550](https://user-images.githubusercontent.com/329257/37872321-3c41d00c-3040-11e8-9835-0bf64af09d7e.jpg)|![zigzag_5557](https://user-images.githubusercontent.com/329257/37872320-3bbea9fc-3040-11e8-948c-418bf54efeee.jpg)

## 5 classes dataset

* 5 class images related with face
    * face, ear, eye, mouth and nose.

```
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/5/train.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/5/test.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/5/answer.csv
```

example:

class|-|-
-|-|-
ear|![ear_1](https://user-images.githubusercontent.com/329257/37873106-7bf94aee-3050-11e8-8cad-1db42782113f.jpg)|![ear_2](https://user-images.githubusercontent.com/329257/37873107-7ecb7512-3050-11e8-940f-7f75e7529644.jpg)
eye|![eye_1](https://user-images.githubusercontent.com/329257/37873109-8963fd50-3050-11e8-96fd-7022962a081c.jpg)|![eye_2](https://user-images.githubusercontent.com/329257/37873110-8989e100-3050-11e8-93a9-8ee2de108f48.jpg)
face|![face_1](https://user-images.githubusercontent.com/329257/37873114-9367b800-3050-11e8-8f45-077328486e5a.jpg)|![face_2](https://user-images.githubusercontent.com/329257/37873115-938e43c6-3050-11e8-9517-c0d0f0678ad9.jpg)
mouth|![mouth_1](https://user-images.githubusercontent.com/329257/37873117-9c6f59b2-3050-11e8-8263-1089f339796e.jpg)|![mouth_2](https://user-images.githubusercontent.com/329257/37873118-9c96aada-3050-11e8-99be-0df56fd28a63.jpg)
nose|![nose_1](https://user-images.githubusercontent.com/329257/37873119-a495e016-3050-11e8-8141-ce0f37612871.jpg)|![nose_2](https://user-images.githubusercontent.com/329257/37873120-a4bad6e6-3050-11e8-84a5-e931d5799940.jpg)

## 41 classes dataset

* Classes whose name starts with "A" or "B".
    * airplane, ambulance, angel, ant, anvil, apple, arm, asparagus, axe, backpack, bandage, barn, bat, bathtub, beach, bear, beard, bed, bee, belt, bench, bicycle, binoculars, bird, blackberry, blueberry, book, boomerang, bottlecap, bowtie, bracelet, brain, bread, bridge, broccoli, broom, bucket, bulldozer, bus, bush, butterfly

```
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/41/train.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/41/test.zip
$ wget -q https://github.com/ikeyasu/circle-zigzag-dataset/releases/download/41/answer.csv
```

example:

class|-|-
-|-|-
airplane|![airplane_1](https://user-images.githubusercontent.com/329257/37873996-47532d02-3062-11e8-85bf-94105c8ec50c.jpg)|![airplane_2](https://user-images.githubusercontent.com/329257/37873997-477a0314-3062-11e8-8a8c-956da159e4a6.jpg)
ambulance|![ambulance_1](https://user-images.githubusercontent.com/329257/37873998-47a0aab4-3062-11e8-9a27-336fe6e24eff.jpg)|![ambulance_2](https://user-images.githubusercontent.com/329257/37873999-47c64b34-3062-11e8-90a1-10020c48e4c0.jpg)
angel|![angel_1](https://user-images.githubusercontent.com/329257/37874000-47ebc97c-3062-11e8-9479-25bfc171fa24.jpg)|![angel_2](https://user-images.githubusercontent.com/329257/37874001-48112032-3062-11e8-8899-80ac23dbc0d1.jpg)
ant|![ant_1](https://user-images.githubusercontent.com/329257/37874002-4839acfa-3062-11e8-85e8-90fcf39f7294.jpg)|![ant_2](https://user-images.githubusercontent.com/329257/37874003-48764d72-3062-11e8-9eca-c30ab5a07f87.jpg)
anvil|![anvil_1](https://user-images.githubusercontent.com/329257/37874004-489d5d86-3062-11e8-80ba-324c9a7197aa.jpg)|![anvil_2](https://user-images.githubusercontent.com/329257/37874005-48c47aa6-3062-11e8-80eb-61326c5dc471.jpg)
apple|![apple_1](https://user-images.githubusercontent.com/329257/37874006-48e719a8-3062-11e8-8b67-13283af9dce9.jpg)|![apple_2](https://user-images.githubusercontent.com/329257/37874007-490c42dc-3062-11e8-86a8-2c7be5a17d05.jpg)
arm|![arm_1](https://user-images.githubusercontent.com/329257/37874008-4933384c-3062-11e8-8111-3b57dc39fe9a.jpg)|![arm_2](https://user-images.githubusercontent.com/329257/37874009-4959dc40-3062-11e8-9abf-6c95e5c375b0.jpg)
asparagus|![asparagus_1](https://user-images.githubusercontent.com/329257/37874010-49807288-3062-11e8-9701-7f1f728e179d.jpg)|![asparagus_2](https://user-images.githubusercontent.com/329257/37874011-49ab31bc-3062-11e8-8ecf-625e8b3da1d6.jpg)
axe|![axe_1](https://user-images.githubusercontent.com/329257/37874012-49d3d6b2-3062-11e8-9a4b-516a27856f90.jpg)|![axe_2](https://user-images.githubusercontent.com/329257/37874013-49fc33f0-3062-11e8-8a18-aaf071cde087.jpg)
backpack|![backpack_1](https://user-images.githubusercontent.com/329257/37874014-4a24509c-3062-11e8-89b7-314d10679ca6.jpg)|![backpack_2](https://user-images.githubusercontent.com/329257/37874015-4a4ad58c-3062-11e8-90ce-2e6bd1e05666.jpg)
bandage|![bandage_1](https://user-images.githubusercontent.com/329257/37874016-4a73b0f6-3062-11e8-8870-8569b8561093.jpg)|![bandage_2](https://user-images.githubusercontent.com/329257/37874017-4a9a49e6-3062-11e8-841a-820587c53c4c.jpg)
barn|![barn_1](https://user-images.githubusercontent.com/329257/37874018-4ac191a4-3062-11e8-8b37-3233ce84ebca.jpg)|![barn_2](https://user-images.githubusercontent.com/329257/37874019-4aeba0de-3062-11e8-9c9d-8b911f3ceb3d.jpg)
bat|![bat_1](https://user-images.githubusercontent.com/329257/37874020-4b10de44-3062-11e8-8922-99e0b259ea89.jpg)|![bat_2](https://user-images.githubusercontent.com/329257/37874021-4b370a2e-3062-11e8-858a-855cf70dd657.jpg)
bathtub|![bathtub_1](https://user-images.githubusercontent.com/329257/37874022-4b5f6032-3062-11e8-919a-e0b9423b2d4f.jpg)|![bathtub_2](https://user-images.githubusercontent.com/329257/37874023-4b884e0c-3062-11e8-8cd0-e9825032c0c7.jpg)
beach|![beach_1](https://user-images.githubusercontent.com/329257/37874024-4bb0909c-3062-11e8-9ec4-1d0c2ec5613b.jpg)|![beach_2](https://user-images.githubusercontent.com/329257/37874025-4bd9fa18-3062-11e8-8a97-16b89c63b9a4.jpg)
bear|![bear_1](https://user-images.githubusercontent.com/329257/37874026-4bff2d4c-3062-11e8-9e4b-24f12b6850dc.jpg)|![bear_2](https://user-images.githubusercontent.com/329257/37874027-4c25ace2-3062-11e8-8469-80dfe8e77922.jpg)
beard|![beard_1](https://user-images.githubusercontent.com/329257/37874029-4c750a44-3062-11e8-9e6e-ea187ea41900.jpg)|![beard_2](https://user-images.githubusercontent.com/329257/37874030-4ca0af1e-3062-11e8-888b-a5a78362e62f.jpg)
bed|![bed_1](https://user-images.githubusercontent.com/329257/37874031-4cc96206-3062-11e8-9401-2d35fe8428c6.jpg)|![bed_2](https://user-images.githubusercontent.com/329257/37874032-4cf4d954-3062-11e8-9b03-1f3fedf57374.jpg)
bee|![bee_1](https://user-images.githubusercontent.com/329257/37874033-4d2180e4-3062-11e8-8261-5dc8e65c488b.jpg)|![bee_2](https://user-images.githubusercontent.com/329257/37874034-4d694e38-3062-11e8-8112-b72baa273301.jpg)
belt|![belt_1](https://user-images.githubusercontent.com/329257/37874035-4da9334a-3062-11e8-8101-bf5653c15313.jpg)|![belt_2](https://user-images.githubusercontent.com/329257/37874036-4dd011f4-3062-11e8-9c50-77cf88b72c95.jpg)
bench|![bench_1](https://user-images.githubusercontent.com/329257/37874037-4dfa4078-3062-11e8-8b89-cf8a2381f8b3.jpg)|![bench_2](https://user-images.githubusercontent.com/329257/37874038-4e24f14c-3062-11e8-805e-6fc2f47bf242.jpg)
bicycle|![bicycle_1](https://user-images.githubusercontent.com/329257/37874039-4e81e80c-3062-11e8-95ae-748f3a501dcb.jpg)|![bicycle_2](https://user-images.githubusercontent.com/329257/37874040-4eba1d76-3062-11e8-953c-940f759d9567.jpg)
binoculars|![binoculars_1](https://user-images.githubusercontent.com/329257/37874041-4ee2aeee-3062-11e8-8138-90aa42591815.jpg)|![binoculars_2](https://user-images.githubusercontent.com/329257/37874042-4f0dbfc6-3062-11e8-9495-ca064ab179c0.jpg)
bird|![bird_1](https://user-images.githubusercontent.com/329257/37874043-4f3baf44-3062-11e8-9867-843a5558cfa5.jpg)|![bird_2](https://user-images.githubusercontent.com/329257/37874044-4f6748b6-3062-11e8-8ac4-5ae727c33f89.jpg)
blackberry|![blackberry_1](https://user-images.githubusercontent.com/329257/37874045-4f8ef794-3062-11e8-92dd-fb077923da14.jpg)|![blackberry_2](https://user-images.githubusercontent.com/329257/37874046-4ffe6f2a-3062-11e8-8a52-63bbf3742348.jpg)
blueberry|![blueberry_1](https://user-images.githubusercontent.com/329257/37874047-50294e02-3062-11e8-86f5-3aa287943526.jpg)|![blueberry_2](https://user-images.githubusercontent.com/329257/37874048-50536cdc-3062-11e8-91e4-bf7b5474769e.jpg)
book|![book_1](https://user-images.githubusercontent.com/329257/37874049-507b6d04-3062-11e8-8e2a-46a68c72047b.jpg)|![book_2](https://user-images.githubusercontent.com/329257/37874050-50a42b90-3062-11e8-8447-d545fc81542e.jpg)
boomerang|![boomerang_1](https://user-images.githubusercontent.com/329257/37874051-50cd3dfa-3062-11e8-90f4-6afaff02a577.jpg)|![boomerang_2](https://user-images.githubusercontent.com/329257/37874052-50f6c5c6-3062-11e8-968a-b65da1bc353d.jpg)
bottlecap|![bottlecap_1](https://user-images.githubusercontent.com/329257/37874053-511e36ec-3062-11e8-8785-4c494043e673.jpg)|![bottlecap_2](https://user-images.githubusercontent.com/329257/37874054-516c76c2-3062-11e8-91be-a41f8cbb8017.jpg)
bowtie|![bowtie_1](https://user-images.githubusercontent.com/329257/37874055-519db1ce-3062-11e8-8254-aedab3a2bc84.jpg)|![bowtie_2](https://user-images.githubusercontent.com/329257/37874056-51c736c0-3062-11e8-82c2-29071546178e.jpg)
bracelet|![bracelet_1](https://user-images.githubusercontent.com/329257/37874057-51f01752-3062-11e8-8755-4225453c8d75.jpg)|![bracelet_2](https://user-images.githubusercontent.com/329257/37874058-521db680-3062-11e8-90e0-3acb2c6748ca.jpg)
brain|![brain_1](https://user-images.githubusercontent.com/329257/37874059-524d05de-3062-11e8-81a7-a7486ace5433.jpg)|![brain_2](https://user-images.githubusercontent.com/329257/37874060-52a12d1c-3062-11e8-97ae-c1b1bbbae4b1.jpg)
bread|![bread_1](https://user-images.githubusercontent.com/329257/37874061-52cb8602-3062-11e8-8ac0-2bae9b9f3961.jpg)|![bread_2](https://user-images.githubusercontent.com/329257/37874062-52f5451e-3062-11e8-870b-cb91dd79f10d.jpg)
bridge|![bridge_1](https://user-images.githubusercontent.com/329257/37874063-531cd872-3062-11e8-93ba-5fdf49303d2d.jpg)|![bridge_2](https://user-images.githubusercontent.com/329257/37874064-5344fe7e-3062-11e8-94b0-f638c55226e5.jpg)
broccoli|![broccoli_1](https://user-images.githubusercontent.com/329257/37874065-536ef8c8-3062-11e8-9136-c66f8c7ba4dc.jpg)|![broccoli_2](https://user-images.githubusercontent.com/329257/37874066-53c17cf6-3062-11e8-8bdc-d3316d60626a.jpg)
broom|![broom_1](https://user-images.githubusercontent.com/329257/37874067-53f19bb6-3062-11e8-9d5f-6228fba66387.jpg)|![broom_2](https://user-images.githubusercontent.com/329257/37874068-541a2612-3062-11e8-94e3-8c0e37f0ebba.jpg)
bucket|![bucket_1](https://user-images.githubusercontent.com/329257/37874069-5442194c-3062-11e8-82c9-4334a33c77d9.jpg)|![bucket_2](https://user-images.githubusercontent.com/329257/37874070-546aa204-3062-11e8-8587-0e28d3a94b98.jpg)
bulldozer|![bulldozer_1](https://user-images.githubusercontent.com/329257/37874071-5496ba2e-3062-11e8-820c-949e90cdf033.jpg)|![bulldozer_2](https://user-images.githubusercontent.com/329257/37874072-54c0b61c-3062-11e8-9af7-f34877710be9.jpg)
bus|![bus_1](https://user-images.githubusercontent.com/329257/37874073-54eb6394-3062-11e8-9062-5e575288fe27.jpg)|![bus_2](https://user-images.githubusercontent.com/329257/37874074-55170af8-3062-11e8-97fa-3164eddf6880.jpg)
bush|![bush_1](https://user-images.githubusercontent.com/329257/37874075-55413c38-3062-11e8-93b5-18c9806e1885.jpg)|![bush_2](https://user-images.githubusercontent.com/329257/37874076-556a2c9c-3062-11e8-95b5-f41ca72b6357.jpg)
butterfly|![butterfly_1](https://user-images.githubusercontent.com/329257/37874077-55925df2-3062-11e8-9c93-d578fd8cdfc0.jpg)|![butterfly_2](https://user-images.githubusercontent.com/329257/37874078-55bcf440-3062-11e8-9fd3-c8b7e3884b51.jpg)


# License

## The Quick, Draw! Dataset

https://github.com/googlecreativelab/quickdraw-dataset/blob/master/LICENSE

```
This data made available by Google, Inc. under the Creative Commons Attribution 4.0 International license.
https://creativecommons.org/licenses/by/4.0/
```

## convert.py

https://github.com/C-Aniruddh/RapidDraw#license

```
Copyright 2017 Aniruddh Chandratre

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

