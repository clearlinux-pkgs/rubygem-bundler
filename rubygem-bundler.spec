#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-bundler
Version  : 1.12.5
Release  : 8
URL      : https://rubygems.org/downloads/bundler-1.12.5.gem
Source0  : https://rubygems.org/downloads/bundler-1.12.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-bundler-bin
BuildRequires : ruby
BuildRequires : rubygem-rdiscount
BuildRequires : rubygem-rdoc

%description
[![Version     ](https://img.shields.io/gem/v/bundler.svg?style=flat)](https://rubygems.org/gems/bundler)
[![Build Status](https://img.shields.io/travis/bundler/bundler/master.svg?style=flat)](https://travis-ci.org/bundler/bundler)
[![Code Climate](https://img.shields.io/codeclimate/github/bundler/bundler.svg?style=flat)](https://codeclimate.com/github/bundler/bundler)
[![Inline docs ](http://inch-ci.org/github/bundler/bundler.svg?style=flat)](http://inch-ci.org/github/bundler/bundler)

%package bin
Summary: bin components for the rubygem-bundler package.
Group: Binaries

%description bin
bin components for the rubygem-bundler package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n bundler-1.12.5
gem spec %{SOURCE0} -l --ruby > rubygem-bundler.gemspec

%build
gem build rubygem-bundler.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
bundler-1.12.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/bundler-1.12.5.gem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/.codeclimate.yml
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/.rubocop_todo.yml
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/CODE_OF_CONDUCT.md
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/DEVELOPMENT.md
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/ISSUES.md
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/LICENSE.md
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/README.md
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/bin/rake
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/bin/rspec
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/bin/rubocop
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/bin/with_rubygems
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/bundler.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/exe/bundle
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/exe/bundle_ruby
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/exe/bundler
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/capistrano.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/binstubs.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/check.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/clean.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/common.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/console.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/exec.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/init.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/inject.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/install.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/lock.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/open.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/outdated.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/package.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/platform.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/show.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/update.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/cli/viz.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/current_ruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/dep_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/dependency.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/deployment.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/deprecate.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/dsl.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/endpoint_specification.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/env.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/environment.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/environment_preserver.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/fetcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/fetcher/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/fetcher/compact_index.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/fetcher/dependency.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/fetcher/downloader.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/fetcher/index.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/friendly_errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/gem_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/gem_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/gem_remote_fetcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/gem_tasks.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/graph.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/index.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/injector.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/inline.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/installer.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/installer/gem_installer.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/installer/parallel_installer.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/installer/standalone.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/lazy_specification.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/lockfile_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-config
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-config.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-exec
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-exec.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-gem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-gem.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-install
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-install.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-lock
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-lock.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-package
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-package.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-platform
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-platform.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-update
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle-update.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/bundle.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/gemfile.5
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/man/gemfile.5.txt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/match_platform.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/mirror.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/psyched_yaml.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/remote_specification.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/resolver.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/retry.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ruby_dsl.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ruby_version.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/rubygems_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/rubygems_gem_installer.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/rubygems_integration.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/runtime.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/settings.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/setup.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/shared_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/similarity_detector.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source/git.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source/git/git_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source/path.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source/path/installer.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source/rubygems.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source/rubygems/remote.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/source_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/spec_set.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/.document
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/Fastly.pem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/GlobalSignOrganizationValidationCA.pem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/GlobalSignRoot.pem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/certificate_manager.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/index.rubygems.org/GlobalSignRoot.pem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/rubygems.global.ssl.fastly.net/DigiCertHighAssuranceEVRootCA.pem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ssl_certs/rubygems.org/AddTrustExternalCARoot-2048.pem
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/stub_specification.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/Executable
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/Executable.standalone
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/.travis.yml.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/CODE_OF_CONDUCT.md.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/Gemfile.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/LICENSE.txt.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/README.md.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/Rakefile.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/bin/console.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/bin/setup.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/exe/newgem.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/ext/newgem/extconf.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/ext/newgem/newgem.c.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/ext/newgem/newgem.h.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/gitignore.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/lib/newgem.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/lib/newgem/version.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/newgem.gemspec.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/rspec.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/spec/newgem_spec.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/spec/spec_helper.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/test/newgem_test.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/templates/newgem/test/test_helper.rb.tt
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ui.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ui/rg_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ui/shell.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/ui/silent.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/compact_index_client/lib/compact_index_client.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/compact_index_client/lib/compact_index_client/cache.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/compact_index_client/lib/compact_index_client/updater.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/compact_index_client/lib/compact_index_client/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/dependency_graph.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/gem_metadata.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/modules/specification_provider.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/modules/ui.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/resolution.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/resolver.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/molinillo/lib/molinillo/state.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/net/http/faster.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/net/http/persistent.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/net/http/persistent/ssl_reuse.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/actions.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/actions/create_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/actions/create_link.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/actions/directory.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/actions/empty_directory.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/actions/file_manipulation.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/actions/inject_into_file.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/command.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/core_ext/hash_with_indifferent_access.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/core_ext/io_binary_read.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/core_ext/ordered_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/error.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/group.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/invocation.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/line_editor.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/line_editor/basic.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/line_editor/readline.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/parser/argument.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/parser/arguments.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/parser/option.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/parser/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/rake_compat.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/shell.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/shell/basic.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/shell/color.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/shell/html.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/util.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendor/thor/lib/thor/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendored_molinillo.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendored_persistent.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vendored_thor.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/vlad.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/lib/bundler/worker.rb
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-config.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-exec.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-gem.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-install.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-lock.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-package.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-platform.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle-update.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/bundle.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/gemfile.5.ronn
/usr/lib64/ruby/gems/2.3.0/gems/bundler-1.12.5/man/index.txt
/usr/lib64/ruby/gems/2.3.0/specifications/bundler-1.12.5.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/bundle
/usr/bin/bundler
