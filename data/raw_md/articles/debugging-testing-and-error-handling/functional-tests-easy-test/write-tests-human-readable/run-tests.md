---
uid: "113210"
seealso: []
title: Run Tests
---
# Run Tests

The test executor utility is a command-line tool that is used to run EasyTest functional tests and produce XML output logs. 

The DevExpress installer includes two TestExecutor utility instances:

    `C:\Program Files\DevExpress <:xx.x:>\Components\Tools\eXpressAppFrameworkNetCore\EasyTest\TestExecutor.v<:xx.x:>.exe`

If a test does not pass, then in addition to the log file, a screenshot (a JPEG file) is created that captures the application's UI state at the time of failure. The following image demonstrates how the test executor works.

![EasyTest_TestExecutor](~/images/easytest_testexecutor116377.png)

> [!NOTE]
> 
> Build your solution in the EasyTest solution configuration before running the TestExecutor tool.
>
> ![easytest solution configuration](~/images/easytest-solution-configuration.png)

The test executor utility has the following command-line syntax:

``TestExecutor.v<:xx.x:>.exe <script_file> | <scripts_dir> [-p:<profile_name>] [-d:<script_line_number_to_stop>] [-l:<LogFileName>] [-o:<alias_name>=<alias_value>]``

| Parameter | Type | Description | Example |
|---|---|---|---|
| **script_file** | Required | Specifies the name of the script file containing the test that must be performed. | ``TestExecutor.v<:xx.x:>.exe D:\MySolution.Tests\ContactTest.ets`` |
| **scripts_dir** | Required | Specifies the name of the directory containing the script files to be executed sequentially. | ``TestExecutor.v<:xx.x:>.exe D:\MySolution.Tests\`` |
| **-p** | Optional | Specifies the [EasyTest configuration](xref:113209) profile that must be used when performing a test. | ``TestExecutor.v<:xx.x:>.exe D:\MySolution.Tests\ContactTest.ets -p:Global`` |
| **-d** | Optional | Specifies that a test script should be run in debug mode. To start script execution, press the ENTER key after the "Press \<Enter> to start test" message is displayed. The script is executed up to the line specified by this parameter's argument. After that, the "Press \<Enter> to process command" message is displayed and you will need to press the ENTER key after each script file line to continue script execution. | ``TestExecutor.v<:xx.x:>.exe D:\MySolution.Tests\ContactTest.ets -d:9`` |
| **-l** | Optional | Specifies the XML log file name. If this parameter is not specified, the log file name specified in the _TestExecutor.v<:xx.x:>.exe.config_ is used. | ``TestExecutor.v<:xx.x:>.exe D:\MySolution.Tests\ContactTest.ets -l:MyLog.xml`` |
| **-o** | Optional | Overrides the value of an alias declared in the [test configuration file](xref:113209). | ``TestExecutor.v<:xx.x:>.exe D:\MySolution.Tests\ContactTest.ets -o:Port=4126`` |
| **-c** | Optional | Specifies the path to the [test configuration file](xref:113209). | ``TestExecutor.v<:xx.x:>.exe D:\MySolution.Tests\ContactTest.ets -c:D:\MySolution.Tests\MyConfig.xml`` |

## Run Multiple Tests in Console

To run a single test script, pass its file name. To sequentially run all test scripts located within a certain directory, pass this directory name.

> [!NOTE]
> To run tests, EasyTest requires a user to be logged in to the UI shell on the test machine.
