{
  'variables': {
    'component': 'shared_library',
    'branding': 'Chromium',
    'chromeos': 0,
    'msan': 0,
    'clang': 0,
    'use_system_yasm': 1,

    'conditions': [
      ['OS=="win"', {
        'os_posix': 0,
        'win_use_allocator_shim': 0,
      }, {
        'os_posix': 1,
      }],
    ]
  },
  'target_defaults': {
    'default_configuration': '<(target_arch)',
    'msvs_cygwin_shell': 0,
    'configurations': {
      'x86_Base': {
        'abstract': 1,
        'msvs_settings': {
          'VCLinkerTool': {
            'SubSystem': '1',
            'MinimumRequiredVersion': '5.01',  # XP.
            'TargetMachine': '1',
          },
          'VCLibrarianTool': {
            'TargetMachine': '1',
          },
        },
        'msvs_configuration_platform': 'x86',
      },
      'x64_Base': {
        'abstract': 1,
        'msvs_settings': {
          'VCLinkerTool': {
            'SubSystem': '1',
            'MinimumRequiredVersion': '5.02',  # Server 2003.
            'TargetMachine': '17', # x86 - 64
          },
          'VCLibrarianTool': {
            'TargetMachine': '17', # x64
          },
        },
        'msvs_configuration_platform': 'x64',
      },
      'Release_Base': {
        'abstract': 1,
        'xcode_settings': {
          'DEAD_CODE_STRIPPING': 'YES',  # -Wl,-dead_strip
          'GCC_OPTIMIZATION_LEVEL': 's',
        },
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': '2', # 2 = /MD (nondebug DLL)
            'Optimization': '2',
            'AdditionalOptions': [
              '/d2Zi+',  # Improve debugging of Release builds.
            ],
          },
          'VCLinkerTool': {
            # LinkIncremental is a tri-state boolean, where 0 means default
            # (i.e., inherit from parent solution), 1 means false, and
            # 2 means true.
            'LinkIncremental': '1',
            # This corresponds to the /PROFILE flag which ensures the PDB
            # file contains FIXUP information (growing the PDB file by about
            # 5%) but does not otherwise alter the output binary. This
            # information is used by the Syzygy optimization tool when
            # decomposing the release image.
            'Profile': 'true',
            'AdditionalDependencies': [
              'advapi32.lib',
            ]
          },
        }
      },
      'x86': {
        'inherit_from': ['x86_Base', 'Release_Base']
      },
      'x64': {
        'inherit_from': ['x64_Base', 'Release_Base']
      }
    }
  }
}