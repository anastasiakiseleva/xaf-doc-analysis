---
uid: "401264"
title: Port an Existing XAF Application to .NET 8+
owner: Alexey Kazakov
seealso:
  - linkType: HRef
    linkId: https://supportcenter.devexpress.com/ticket/details/t985962/core-xaf-s-blazor-and-winforms-net-core-assemblies-target-net-5
    altText: XAF ASP.NET Core Blazor and WinForms (.NET Core) assemblies target .NET 5
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/porting/
    altText: Overview of porting from .NET Framework to .NET
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/compatibility/10.0
    altText: Breaking changes in .NET 10
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/compatibility/9.0
    altText: Breaking changes in .NET 9
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/compatibility/8.0
    altText: Breaking changes in .NET 8
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/compatibility/7.0
    altText: Breaking changes in .NET 7
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/compatibility/6.0
    altText: Breaking changes in .NET 6
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/dotnet/core/compatibility/5.0
    altText: Breaking changes in .NET 5
  - linkType: HRef
    linkId: https://learn.microsoft.com/en-us/aspnet/core/migration/31-to-50
    altText: 'Migrate from ASP.NET Core 3.1 to 5.0'
---
# Port an Existing XAF Application to .NET 8+

Assemblies, demos, and project templates for XAF ASP.NET Core Blazor and WinForms (.NET Core) v<:xx.x:> target **.NET 8**. For more information, review the following breaking change ticket: [.NET 8 and .NET Framework 4.6.2 are minimally supported Target Frameworks for DevExpress libraries in v24.2](https://supportcenter.devexpress.com/ticket/details/t1245925/net-8-and-net-framework-4-6-2-are-minimally-supported-target-frameworks-for-devexpress). Install Visual Studio 17.0 or higher to use .NET.

This topic explains how to update your existing XAF solution to .NET.

> [!Important]
> Copy and save the current versions of all *csproj* files before porting.

## Port an XAF WinForms App from .NET Framework to .NET 8+

Make sure that your XAF WinForms application can be migrated to .NET and all the required components are installed on your machine. For details, refer to the following topic: <xref:401253>. 
 
Follow the steps below to port the application:


1. In the Solution Explorer, unload all projects.

2. Replace the existing code in each *csproj* file with the following:

    **MySolution.Module**

    # [XML](#tab/tabid-xml)

    ```XML
    <Project Sdk="Microsoft.NET.Sdk">
        <PropertyGroup>
            <TargetFramework>net8.0</TargetFramework>
            <RootNamespace>MySolution.Module</RootNamespace>
            <Deterministic>False</Deterministic>
        </PropertyGroup>
        <ItemGroup>
            <EmbeddedResource Include="**\*.svg" />
            <EmbeddedResource Include="**\*.xafml" />
            <EmbeddedResource Remove="bin\**" />
        </ItemGroup>
        <ItemGroup>
            <PackageReference Include="DevExpress.ExpressApp" Version="<:xx.x.x:>" />
        </ItemGroup>
    </Project>
    ```
    ***


    **MySolution.Module.Win**

    # [XML](#tab/tabid-xml)

    ```XML
    <Project Sdk="Microsoft.NET.Sdk">
        <PropertyGroup>
            <TargetFramework>net8.0-windows</TargetFramework>
            <Deterministic>False</Deterministic>
        </PropertyGroup>
        <ItemGroup>
            <EmbeddedResource Include="**\*.svg" />
            <EmbeddedResource Include="Model.DesignedDiffs.xafml" />
            <EmbeddedResource Remove="bin\**" />
        </ItemGroup>
        <ItemGroup>
            <ProjectReference Include="..\MySolution.Module\MySolution.Module.csproj" />
        </ItemGroup>
    </Project>
    ```
    ***

    **MySolution.Win** 

    # [XML](#tab/tabid-xml)

    ```XML
    <Project Sdk="Microsoft.NET.Sdk">
        <PropertyGroup>
            <OutputType>WinExe</OutputType>
            <TargetFramework>net8.0-windows</TargetFramework>
            <Deterministic>False</Deterministic>
        </PropertyGroup>
        <ItemGroup>
            <Content Include="Model.xafml">
                <CopyToOutputDirectory>Always</CopyToOutputDirectory>
            </Content>
            <EmbeddedResource Include="**\*.svg" />
            <EmbeddedResource Remove="bin\**" />
        </ItemGroup>
        <ItemGroup>
            <ProjectReference Include="..\MySolution.Module.Win\MySolution.Module.Win.csproj" />
            <ProjectReference Include="..\MySolution.Module\MySolution.Module.csproj" />
        </ItemGroup>
    </Project>
    ```
    ***

3. In the new code, replace the "MySolution" placeholder with your project's root namespace in the `<RootNamespace>` element and with the project's name in the `<ProjectReference>` element. 

4. If you reference other projects or NuGet packages, copy corresponding `<ProjectReference>` elements from the old version of the *csproj* files and paste them into the new version.

5. If your projects require other resources (for example, _PNG_ images), include them in `<EmbeddedResource>` elements.

6. Reload all projects.

7. In the _Program.cs_ file, comment the following line:

    # [C#](#tab/tabid-csharp)

    ```csharp
    static class Program {
        // ...
        static void Main() {
            // ...
            EditModelPermission.AlwaysGranted = System.Diagnostics.Debugger.IsAttached;
        }
    }
    ```

    ***

8. In the *App.config* file, remove the `<system.diagnostics>` element and add the code below to `<appSettings>`:

    # [XML](#tab/tabid-xml)

    ```XML
    <?xml version="1.0"?>
    <configuration>
    <!-- ... -->
        <appSettings>
        <!-- ... -->
            <add key="eXpressAppFrameworkTraceLevel" value="3"/>
        </appSettings>
    </configuration>
    ```
    ***

    .NET applications use this key instead of [switches](xref:112575#log-files-generated-at-runtime) in the `<system.diagnostics>` element.

   If you use EasyTest in your application, add the following keys:

    # [XML](#tab/tabid-xml)

    ```XML
    <?xml version="1.0"?>
    <configuration>
    <!-- ... -->
        <appSettings>
        <!-- ... -->
            <add key="EasyTestTraceLevel" value="4"/> 
            <add key="EasyTestLogFileName" value="TestExecutor.log" />
        </appSettings>
    </configuration>
    ```
    ***

9. _Optional_. Enable [the latest framework settings](xref:DevExpress.ExpressApp.FrameworkSettings.DefaultSettingsCompatibilityMode) at the top of the `Main` method:

    # [C#](#tab/tabid-csharp)
    
    ```csharp
    namespace MySolution.Win {
        static void Main() {
            DevExpress.ExpressApp.FrameworkSettings.DefaultSettingsCompatibilityMode = DevExpress.ExpressApp.FrameworkSettingsCompatibilityMode.Latest;
            // ...
        }
    }
    ```
    
    ***

10. Rebuild the solution.

11. If you port an EF 6-based application, you also need to move to EF Core because .NET applications do not support EF 6. This move may require additional changes to your application. For more information, refer to the following article: [Port from EF6 to EF Core](https://learn.microsoft.com/en-us/ef/efcore-and-ef6/porting/).

> [!Note]
> Refer to the following topic for information on how to deploy the ported application: [](xref:401276).

## Port an XAF App from .NET 6 to .NET 8+

If you are migrating from .NET 6 to .NET 8+, you can use the [Project Converter](xref:2529) to simplify your migration (the Project Converter automatically retargets your projects to .NET 8 and updates third-party NuGet packages in projects that depend on DevExpress libraries).

<!-- 
## Semi-Automatic Migration with the Project Converter

To simplify the migration process, the DevExpress [Project Converter](xref:2529) attempts to retarget your XAF projects to .NET automatically. 

> [!NOTE]
> 
> Our **Project Converter** does not update your non-XAF projects, custom dependencies, or code. You need to complete .NET migration manually. -->
