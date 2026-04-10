This topic contains step-by-step instructions on how to create an ASP.NET Core Blazor or WinForms application with Middle Tier Security.

1. Use the [DevExpress Template Kit](xref:405447) to create a new solution in Visual Studio.

    ![Create a new project with Template Kit](~/images/template-kit/template-kit-create-a-new-project.png)

1. Specify the project name and location, and click **Create**.
1. In the invoked **Template Kit** window, select XAF.
1. Select the following options:
    * ORM: **<:0:>**
    * Platforms: **Web (ASP.NET Core Blazor)**, or **Desktop (Windows Forms)**, or both.
    * Security Options: **Standard (requests login and password)** and **Middle Tier Security - No direct database access**

    ![Template Kit with specified options](~/images/template-kit/template-kit-middle-tier-options.png)

1. _Optional._ Select additional [XAF modules](xref:118046).
1. Click **Create Project**.

    XAF generates a solution with the following projects:

    | Name | Description |
    |------|-------------|
    | _MySolution.Blazor.Server_ (if selected) | The Blazor Application project |
    | _MySolution.MiddleTier_ | The Middle Tier Service project |
    | _MySolution.Module_ | The Module project |
    | _MySolution.Win_ (if selected) | The WinForms Application project |

1. Run the application:
    * For Blazor, run MiddleTier project, then run the Blazor project.
    * For WinForms, run the WinForms project.