import argparse
import json


class CmdLineOptions(object):

    Purpose = ("qtp", "regression", "bvt", "sit", "dev", "nst", "svt", "fav", "sustaining")

    @staticmethod
    def define(parser, services):

        #
        # General Tool Options
        #
        general_parsing = argparse.ArgumentParser(add_help=False)

        general_group = general_parsing.add_argument_group("General Tool Options")

        general_group.add_argument("-t", "--tests",
                                   action="append",
                                   dest="tests",
                                   help="Test file to load",
                                   default=[])
        general_group.add_argument("-s", "--suites",
                                   action="append",
                                   dest="suite_files",
                                   help="Suite file to load",
                                   default=[])
        general_group.add_argument("-c", "--config",
                                   action="append",
                                   dest="config_files",
                                   help="Extra configuration files to load",
                                   default=[])
        general_group.add_argument("--setting",
                                   action="append",
                                   dest="cmdline_settings",
                                   help="Key/Value settings which override internal settings",
                                   default=[])
        general_group.add_argument("-d", "--debug",
                                   action="store",
                                   dest="debug",
                                   choices=['0', '1', '2'],
                                   help="Enable test debug logging: Levels = 0,1,2",
                                   default=None)
        general_group.add_argument("--tool-debug",
                                   action="store",
                                   dest="debug_tool",
                                   choices=['0', '1', '2'],
                                   help="Enable tool debug logging: Levels = 0,1,2",
                                   default=None)
        general_group.add_argument("-n", "--name",
                                   action="store",
                                   dest="session_name",
                                   default=None,
                                   help="Specify a Session Name for the invocation. Default = {username}.{datetime}")

        #
        # Logging Options
        #
        log_parsing = argparse.ArgumentParser(add_help=False)

        l_group = log_parsing.add_argument_group("Logging Options")
        l_group.add_argument("-l", "--log",
                             action="store",
                             dest="log_file",
                             help="Save tool logging information to the specified file",
                             default=None)
        l_group.add_argument("--log-disable",
                             action="store_true",
                             dest="log_disabled",
                             help="Disable automatic log file output",
                             default=False)
        l_group.add_argument("--log-dir",
                             action="store",
                             dest="log_dir",
                             help="Save test specific log files in this directory, default: /syzygy/logs/{username}/<run.name>",
                             default=None)

        #
        # Test Execution Options
        #
        exec_parsing = argparse.ArgumentParser(add_help=False)

        exec_group = exec_parsing.add_argument_group("Test Execution Options")
        exec_group.add_argument("-p", "--purpose",
                                action="store",
                                dest="purpose",
                                help="What is the purpose of this run: {}".format(", ".join(CmdLineOptions.Purpose)),
                                default=None)
        exec_group.add_argument("--run-start",
                                action="store",
                                dest="run_start_at_node",
                                help="Start the run at a specific Collection Node. For example: --run-start=//Path/Name",
                                default=None)
        exec_group.add_argument("--repeat-count",
                                action="store",
                                type=int,
                                dest="repeat_count",
                                help="Repeat the tool run for the specified count. Default = 1",
                                default=1)
        exec_group.add_argument("--repeat-time",
                                action="store",
                                dest="repeat_time",
                                help="Repeat the tool run for the given amount of time",
                                default=0.0)
        exec_group.add_argument("--repeat-forever",
                                action="store_true",
                                dest="repeat_forever",
                                help="Repeat the tool run forever",
                                default=False)
        exec_group.add_argument("--repeat-period",
                                action="store",
                                dest="repeat_period",
                                help="Repeat the tool run at a specified period",
                                default=0.0)
        exec_group.add_argument("--repeat-on-ef",
                                action="store_true",
                                dest="repeat_on_ef",
                                help="Repeat the tests with an error or failure state",
                                default=False)

        sequence_list = "a|b|c"
        default_sequence = "sequence"

        exec_group.add_argument("--run-sequence",
                                action="store",
                                dest="run_sequence",
                                help="Specify the sequence mode: {}, default={}".format(sequence_list, default_sequence),
                                default=False)
        exec_group.add_argument("--random-seed",
                                action="store",
                                type=int,
                                dest="random_seed",
                                help="Define the test tool wide random seed",
                                default=None)

        #
        # Section Commands
        #
        subparsers = parser.add_subparsers(title="Section Commands", dest="command")

        # Make the Run command

        run_parser = subparsers.add_parser("run", help="Run a test",
                                           parents=[general_parsing, log_parsing, exec_parsing])
        #run_parser.set_defaults(func=run.RunCommand.make)

        run_parser.add_argument("--no-verify", action="store_true", default=False, help="Do not verify tests before running")

        # Make the Test command

        test_parser = subparsers.add_parser("tests", help="Commands related to test information")
        test_subparsers = test_parser.add_subparsers(dest="test_command")

        test_list_parser = test_subparsers.add_parser("list", help="List the test to be run",
                                                      parents=[general_parsing, exec_parsing, log_parsing])
        #test_list_parser.set_defaults(func=tests.ListTests.make)

        test_dump_parser = test_subparsers.add_parser("dump", help="Dump the test tree data",
                                                      parents=[general_parsing])
        #test_dump_parser.set_defaults(func=tests.DumpTestTreeCommand.make)

        test_verify_parser = test_subparsers.add_parser("verify", help="Verify the test can execute (but do not run)",
                                                        parents=[general_parsing])
        #test_verify_parser.set_defaults(func=tests.VerifyTestsCommand.make)

        test_parser.set_defaults(usage=test_parser.print_help)
        # Make the Settings command

        settings_parser = subparsers.add_parser("settings", help="Show the settings for the test tool",
                                                parents=[general_parsing, log_parsing, exec_parsing])
        #settings_parser.set_defaults(func=settings.DumpSettingsCommand.make)

        # Default behavior
        parser.set_defaults(usage=parser.print_help)

        #
        # Add to general Services
        #

        services.setdefault("parsers", {})
        services['parsers'].update({
            'options.general': general_parsing,
            'options.log': log_parsing,
            'options.exec': exec_parsing,
            'main': parser,
            'main.subparsers': subparsers,
            'run': run_parser,
            'tests': test_parser,
            'tests.subparsers': test_subparsers,
            'tests.list': test_list_parser,
            'tests.dump': test_dump_parser,
            'tests.verify': test_verify_parser,
            'settings': settings_parser
        })

        return services['parsers']


parser = argparse.ArgumentParser()
services = {}
r = CmdLineOptions.define(parser, services)

#for k, v in sorted(services['parsers'].items()):
    #print('{}: {}'.format(k, v))

#o = parser.parse_args()
o = r['main'].parse_args()
print(o)

