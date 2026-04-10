## How to Suppress this Warning

Refer to the following Microsoft article to learn how to suppress warning messages for a specific project: [How to: Suppress compiler warnings](https://learn.microsoft.com/en-us/visualstudio/ide/how-to-suppress-compiler-warnings#suppress-specific-warnings-for-visual-c-or-f).

To suppress warning messages for all projects in a solution, follow the steps below:

1. Open the _"Directory.Build.props"_ file or create it in the root directory of your solution. For more information, refer to the following article: [Customize your build: Directory.Build.props and Directory.Build.targets](https://learn.microsoft.com/en-us/visualstudio/msbuild/customize-your-build#directorybuildprops-and-directorybuildtargets).
2. In the **NoWarn** section, specify codes of warnings that you want to suppress. Use semicolons to separate codes:
    
    # [XML](#tab/tabid-xml)
    ```XML
    <Project>
      <PropertyGroup>
        <NoWarn>XAF0006;XAF0007</NoWarn>
      </PropertyGroup>
    </Project> 
    ```
    ***
