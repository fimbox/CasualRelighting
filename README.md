# CasualRelighting

We present a method for recovering both incident lighting and surface materials from
casually scanned geometry. By casual, we mean a rapid and potentially noisy scanning
procedure of unmodified and uninstrumented scenes with a commodity RGB-D sensor.
In other words, unlike reconstruction procedures which require careful preparations in a
laboratory environment, our method works with input that can be obtained by consumer
users. To ensure a robust procedure, we segment the reconstructed geometry into surfaces
with homogeneous material properties and compute the radiance transfer on these
segments. With this input, we solve the inverse rendering problem of factorization into
lighting and material properties using an iterative optimization in spherical harmonics
form. This allows us to account for self-shadowing and recover specular properties of
Phong-like materials. The resulting data can be used to generate a wide range of mixed
reality applications, including the rendering of synthetic objects with matching lighting
into a given scene, but also re-rendering the scene (or a part of it) with new lighting. We
show the robustness of our approach with real and synthetic examples under a variety of
lighting conditions and compare them with ground truth data.

![](https://raw.githubusercontent.com/fimbox/CasualRelighting/master/doc/img/relighting_title_image.jpg)

# Publication:
[Instant Relighting ISMAR 2016](https://github.com/fimbox/CasualRelighting/blob/master/doc/Instant_Relighting_ISMAR_2016.pdf)


Thomas Richter-Trummer, Denis Kalkofen, Jinwoo Park, Dieter Schmalstieg, "Instant Mixed Reality Lighting from Casual Scanning", 2016 IEEE International Symposium on Mixed and Augmented Reality (ISMAR), vol. 00, no. , pp. 27-36, 2016, doi:10.1109/ISMAR.2016.18

## bibtex:
https://ieeecs-services.computer.org/csdl/citation/proceedings/bibtex/ismar/2016/3641/00/3641a027

