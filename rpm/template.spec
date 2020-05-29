%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-rosmon-core
Version:        2.3.2
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rosmon_core package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python3-devel
Requires:       ncurses-devel
Requires:       ros-noetic-cmake-modules
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-rosbash
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-rosfmt
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rosmon-msgs
Requires:       ros-noetic-rospack
Requires:       ros-noetic-std-msgs
Requires:       tinyxml-devel
Requires:       yaml-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  python3-rospkg
BuildRequires:  ros-noetic-catch-ros
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-rosbash
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rosfmt
BuildRequires:  ros-noetic-roslib
BuildRequires:  ros-noetic-rosmon-msgs
BuildRequires:  ros-noetic-rospack
BuildRequires:  ros-noetic-rostest
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  tinyxml-devel
BuildRequires:  yaml-cpp-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Node launcher and monitor for ROS. rosmon is a replacement for the roslaunch
tool, focused on performance, remote monitoring, and usability.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Fri May 29 2020 Max Schwarz <max.schwarz@uni-bonn.de> - 2.3.2-1
- Autogenerated by Bloom

* Thu May 28 2020 Max Schwarz <max.schwarz@uni-bonn.de> - 2.3.1-1
- Autogenerated by Bloom

* Thu May 28 2020 Max Schwarz <max.schwarz@uni-bonn.de> - 2.3.0-1
- Autogenerated by Bloom

