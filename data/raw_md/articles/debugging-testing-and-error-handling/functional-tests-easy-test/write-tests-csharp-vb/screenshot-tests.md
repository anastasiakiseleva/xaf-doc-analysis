---
uid: "403972"
title: 'Screenshot Tests (Visual Testing)'
owner: Alexey Kazakov
---
# Screenshot Tests (Visual Testing)

EasyTest supports screenshot testing for XAF ASP.NET Core Blazor and Windows Forms. This topic explains how to run screenshot tests.

## Add a Visual Test

The steps below show how to add a visual test for the login form.

1. In your test project, create a _Screenshots_ folder, and add an expected image (_{BlazorAppName}_Login.png_) and a mask image (_{BlazorAppName}_Login_Mask.png_). In the properties window, set the **Build Action** property for these images to **Embedded resource**.

2. Add the following code to get an image from the embedded resources:

    # [C#](#tab/tabid-csharp1)
    
    ```csharp
    using System.Reflection;

    // ...

    private static Image LoadImageFromResource(string searchPattern) {
        var assembly = Assembly.GetExecutingAssembly();
        var resourceName = assembly.GetManifestResourceNames().FirstOrDefault(x => x.Contains(searchPattern));
        using var stream = assembly.GetManifestResourceStream(resourceName);
        if(stream is not null) {
            return Image.FromStream(stream);
        }
        return null;
    }
    ```
    ***
3. The following method saves an image to a file:

    # [C#](#tab/tabid-csharp1)
    
    ```csharp
    using System.Drawing.Imaging;
    using System.IO;

    // ...

    private static void SaveImage(Image image, string folder, string fileName, string postfix) {
        if(!Directory.Exists(folder)) {
            Directory.CreateDirectory(folder);
        }
        string fileNameWithoutExtension = Path.Combine(folder, Path.GetFileNameWithoutExtension(fileName));
        string actualFileName = string.Format("{0}.{1}{2}", fileNameWithoutExtension, postfix, Path.GetExtension(fileName));
        image.Save(actualFileName, ImageFormat.Png);
    }
    ```
    ***

4. Add test code:

    # [C#](#tab/tabid-csharp1)
    
    ```csharp
    const string BlazorAppName = "MyAppNameBlazor";

    // ...
    [Fact]
    public void ScreenshotTest() {
        var outputDirectory = Environment.CurrentDirectory;
        IApplicationContext appContext = FixtureContext.CreateApplicationContext(BlazorAppName);
        appContext.RunApplication();
        string expectedImageName = $"{BlazorAppName}_Login.png";
        string maskImageName = $"{BlazorAppName}_Login_Mask.png";
        Image expectedImage = LoadImageFromResource(expectedImageName);
        Image maskImage = LoadImageFromResource(maskImageName);

        // Call the SetActiveWindowsSize method to ensure the actual 
        // and the expected image have the same dimensions.
        appContext.GetScreen().SetActiveWindowSize(new Size(1024, 768));
        
        // Get the actual screenshot.
        Image screenshot = appContext.GetScreen().GetScreenshot();
        
        // Compare the expected image with the actual image.
        bool equality = appContext.GetScreen().ImagesEqual(screenshot, expectedImage, maskImage);

        // If the images are not equal, save the actual image and a diff image.
        if(!equality) {
            Image diffs = appContext.GetScreen().GetImagesDifferences(screenshot, expectedImage, maskImage);
            SaveImage(screenshot, outputDirectory, expectedImageName, "Actual");
            SaveImage(diffs, outputDirectory, expectedImageName, "Diff");
        }
        Assert.True(equality);
    }
    ```
    ***

## Image Types

Expected image
:    The screenshot test compares an actual screenshot with an expected image. The expected image captures the application's visual state you need to achieve during the test.

     ![|easytest-screenshot-test-original-image](~/images/easytest-screenshot-test-original-image.png)

Mask image
:    Use a mask image to ignore a particular area on the screenshot (for example, a text input with a blinking cursor). Mask images are of the same size as their corresponding expected images. A mask image has a white background; ignored areas are painted in black.

     ![|easytest-screenshot-test-mask-image](~/images/easytest-screenshot-test-mask-image.png)

Diff image
:    A diff image shows the difference between expected and actual images. The different areas are painted red.

     ![|easytest-screenshot-test-mask-image](~/images/easytest-screenshot-test-diff-image.png)

Actual image (Screenshot)
:    An application screenshot captured during testing. If the actual image is the same as the expected image, the test passed.
