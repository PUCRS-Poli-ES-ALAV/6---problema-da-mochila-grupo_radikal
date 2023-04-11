# Editing Distance Problem

## Case 0
$s_1 =$ "Casablanca"
$s_2 =$ "Portentoso"

**Cost = 10**

|   **Case 0**   |     **Brute Force**    |    **Dynamic Programming**    |
|:--------------:|:----------------------:|:-----------------------------:|
|  **Time (s)**  |    3.131366491317749   |     0.00011777877807617188    |
| **Iterations** |        10100193        |               81              |

## Case 1
$s_1 =$ "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to simplify the build processes in the Jakarta Turbine project. There were several projects, each with their own Ant build files, that were all slightly different. JARs were checked into CVS. We wanted a standard way to build the projects, a clear definition of what the project consisted of, an easy way to publish project information and a way to share JARs across several projects. The result is a tool that can now be used for building and managing any Java-based project. We hope that we have created something that will make the day-to-day work of Java developers easier and generally help with the comprehension of any Java-based project."
$s_2 =$ "This post is not about deep learning. But it could be might as well. This is the power of kernels. They are universally applicable in any machine learning algorithm. Why you might ask? I am going to try to answer this question in this article. Go to the profile of Marin Vlastelica Pogančić Marin Vlastelica Pogančić Jun"

**Cost = 557**

|   **Case 1**   |    **Dynamic Programming**    |
|:--------------:|:-----------------------------:|
|  **Time (s)**  |      0.14423704147338867      |
| **Iterations** |            226653             |
